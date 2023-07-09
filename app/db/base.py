# Import all the models, so that Base has them before being

from app.db.base_class import Base
from app.models.product import Product
from app.models.feedback import Feedback
from app.models.suggested import Suggested
