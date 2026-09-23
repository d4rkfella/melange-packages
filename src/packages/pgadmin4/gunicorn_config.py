import os
import gunicorn

from config import JSON_LOGGER, CONSOLE_LOG_LEVEL, CONSOLE_LOG_FORMAT_JSON

gunicorn.SERVER_SOFTWARE = "Python"

# Include the authenticated user identity in the access log.
# %({x-remote-user}o)s reads the X-Remote-User response header set by pgAdmin
# for authenticated requests; unauthenticated requests log '-'.
access_log_format = (
    '%(h)s %(l)s %({x-remote-user}o)s %(t)s "%(r)s" %(s)s %(b)s '
    '"%(f)s" "%(a)s"'
)

if JSON_LOGGER:
    logconfig_dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {"level": CONSOLE_LOG_LEVEL, "handlers": []},
        "loggers": {
            "gunicorn.error": {
                "level": CONSOLE_LOG_LEVEL,
                "handlers": ["error_console"],
                "propagate": True,
                "qualname": "gunicorn.error",
            },
            "gunicorn.access": {
                "level": CONSOLE_LOG_LEVEL,
                "handlers": ["console"],
                "propagate": True,
                "qualname": "gunicorn.access",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "json",
                "stream": "ext://sys.stdout",
            },
            "error_console": {
                "class": "logging.StreamHandler",
                "formatter": "json",
                "stream": "ext://sys.stderr",
            },
        },
        "formatters": {
            "json": {
                "class": "jsonformatter.JsonFormatter",
                "format": CONSOLE_LOG_FORMAT_JSON,
            },
        },
    }

control_socket_disable = True

bind = "{}:{}".format(
    os.environ.get("PGADMIN_LISTEN_ADDRESS", "0.0.0.0"),
    os.environ.get(
        "PGADMIN_LISTEN_PORT",
        "443" if os.environ.get("PGADMIN_ENABLE_TLS") else "80",
    ),
)

if os.environ.get("PGADMIN_ENABLE_TLS"):
    keyfile = os.environ.get(
        "PGADMIN_TLS_KEYFILE",
        "/certs/server.key",
    )
    certfile = os.environ.get(
        "PGADMIN_TLS_CERTFILE",
        "/certs/server.cert",
    )

workers = int(os.environ.get("GUNICORN_WORKERS", "1"))
threads = int(os.environ.get("GUNICORN_THREADS", "25"))

timeout = int(os.environ.get("GUNICORN_TIMEOUT", "60"))

limit_request_line = int(
    os.environ.get("GUNICORN_LIMIT_REQUEST_LINE", "8190")
)
limit_request_fields = int(
    os.environ.get("GUNICORN_LIMIT_REQUEST_FIELDS", "100")
)
limit_request_field_size = int(
    os.environ.get("GUNICORN_LIMIT_REQUEST_FIELD_SIZE", "8190")
)
