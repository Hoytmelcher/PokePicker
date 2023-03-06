from flask import Blueprint

bp = Blueprint('poke', __name__, url_prefix='/poke')

from . import routes, models