from os import environ

FLASK_ENV = environ.get("FLASK_ENV")

match FLASK_ENV:
    case "development":
        from config.development import DevelopmentConfig as Config  # noqa
    case "dev":
        pass
    case "test":
        pass
    case "production":
        pass
    case _:
        from config.default import DefaultConfig as Config  # noqa

try:
    Config.pretty_print()
except AttributeError:
    print({"msg": "Config doesn't have pretty_print function."})
