from flask import Blueprint
from flask import render_template

default_bp = Blueprint(
    "default_bp", __name__, url_prefix="/default", template_folder="templates"
)


@default_bp.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@default_bp.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500
