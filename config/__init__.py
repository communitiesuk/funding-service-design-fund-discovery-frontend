from os import environ

FLASK_ENV = environ.get("FLASK_ENV")

match FLASK_ENV:
    case "dev":
        from config.dev import DevConfig as Config  # noqa
    case "development":
        from config.development import DevelopmentConfig as Config  # noqa
    case "test":
        from config.test import TestConfig as Config  # noqa
    case "unit_test":
        from config.unit_test import UnitTestConfig as Config  # noqa
    case "production":
        pass
    case _:
        from config.default import DefaultConfig as Config  # noqa

try:
    Config.pretty_print()
except AttributeError:
    print({"msg": "Config doesn't have pretty_print function."})

__all__ = [Config]
