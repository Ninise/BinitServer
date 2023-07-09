import random
import string
from typing import Dict


def random_city() -> str:
    return random.choice(["Toronto", "Ottawa", "Oshawa", "Whitby", "Ajax"])


def random_product_type() -> str:
    return random.choice(["ORGANIC", "GARBAGE", "RECYCLE", "HAZARD", "ELECTRO"])


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"
