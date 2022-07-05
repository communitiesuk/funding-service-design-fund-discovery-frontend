from flask import Flask
from flask_compress import Compress
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from fsd_utils.logging import logging
from config import Config
from jinja2 import ChoiceLoader
from jinja2 import PackageLoader
from jinja2 import PrefixLoader


def create_app() -> Flask:
    """Returns the initialised flask app."""

    flask_app = Flask("Fund Discovery Frontend", static_url_path="/assets")

    flask_app.config.from_object("config.Config")

    flask_app.jinja_loader = ChoiceLoader(
        [
            PackageLoader("app"),
            PrefixLoader(
                {"govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja")}
            ),
        ]
    )

    flask_app.jinja_env.trim_blocks = True
    flask_app.jinja_env.lstrip_blocks = True

    # Initialise logging
    logging.init_app(flask_app)

    # Configure application security with Talisman
    Talisman(flask_app, **Config.TALISMAN_SETTINGS)

    csrf = CSRFProtect()

    csrf.init_app(flask_app)

    @flask_app.context_processor
    def inject_global_constants():
        return dict(
            stage="beta",
            service_title="Funding Service Design - Discovery Hub",
            service_meta_description=(
                "Funding Service Design Iteration - Discovery Hub"
            ),
            service_meta_keywords="Funding Service Design - Discovery Hub",
            service_meta_author="DLUHC",
        )

    from app.default.error_routes import (
        default_bp,
        not_found,
        internal_server_error,
    )
    from app.discovery.routes import discovery_bp

    # register routes
    flask_app.register_error_handler(404, not_found)
    flask_app.register_error_handler(500, internal_server_error)
    flask_app.register_blueprint(default_bp)
    flask_app.register_blueprint(discovery_bp)

    return flask_app


app = create_app()
