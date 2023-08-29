# Get all products in a db
# Check if item has an image
# if not make a request to pexels
# get a first image from list
# download it
# save to folder with assets
# save image url to the product
# start over

import asyncio
import aiohttp

from app import crud
from app.utils import deps
from app.db.session import SessionLocal
from app.schemas.product import ProductUpdate

import requests
import os

db = SessionLocal()


async def fetch_image_from_external_source(product):
    async with aiohttp.ClientSession(trust_env=True) as session:
        url = f"https://api.pexels.com/v1/search?query={product.name}&per_page=3"
        headers = {
            "Authorization": "Aqu4ER77lQgPsFo771e2Q4QfMDEqPhIa4qWToUO7DM97R7N0WbJdpu37"
        }
        print("fetch image")
        async with session.get(url, headers=headers, ssl=False) as response:
            if response.status == 200:
                print("response 200")
                data = await response.json()
                photos = data.get("photos", [])
                if len(photos) > 0:
                    print(photos[0]["src"]["original"])
                    return photos[0]["src"]["original"]
                else:
                    print("No photo found")
                    return ""
            else:
                print(f"Error: {response.status} - {await response.text()}")
                return ""


async def process_product(product):
    print("process_product 1")
    if not product.image:
        print("no image found ${product.name} " + product.name)
        image_path = await fetch_image_from_external_source(product)
        if image_path:
            print('image to update ' + product.name)
            # Update the product in the database
            product_updated = crud.product.update(
                db=db, db_obj=product, obj_in=ProductUpdate(image=image_path))
            print('product updated ' + product_updated.name +
                  ' - ' + product_updated.image)


async def main():
    # Create a database session

    try:
        items = crud.product.get_all(db=db)

        # Create a list of asynchronous tasks
        # tasks = [process_product(product) for product in items]
        # tasks = [process_product(items[0])]
        tasks = []
        task_interval = 3600 / 200  # 1 hour / number of tasks
        for product in items:
            # Sleep to control the task rate
            await asyncio.gather(*[process_product(product)])
            await asyncio.sleep(task_interval)

        # Run the asynchronous tasks concurrently

    finally:
        # Close the database session to release resources
        db.close()

# Run the asynchronous event loop
asyncio.run(main())
