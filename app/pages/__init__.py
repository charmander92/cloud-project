from Flask import Bluepring

pages = Blueprint('pages', __name__)

from . import routes
