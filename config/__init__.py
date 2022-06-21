from os import environ

FLASK_ENV = environ.get("FLASK_ENV")

if FLASK_ENV == "development":
    from config.development import DevelopmentConfig as Config  # noqa

    Config.pretty_print()
elif FLASK_ENV == "dev":
    pass
elif FLASK_ENV == "test":
    pass
elif FLASK_ENV == "production":
    pass
else:
    from config.default import DefaultConfig as Config  # noqa
