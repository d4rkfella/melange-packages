import ast
import os

###############################################################################
# Wolfi distribution / filesystem configuration
###############################################################################

UPGRADE_CHECK_ENABLED = False

# System CA bundle provided by Wolfi's ca-certificates package.
CA_FILE = os.environ.get(
    "SSL_CERT_FILE",
    "/etc/ssl/certs/ca-certificates.crt",
)

# Do not write application logs into the image filesystem.
LOG_FILE = "/dev/null"

# Documentation is installed as a sibling of the pgAdmin application
# directory:
#
#   /usr/lib/pgadmin4/
#   /usr/lib/pgadmin4/docs/
#
HELP_PATH = "../../docs"


###############################################################################
# PostgreSQL client binaries
###############################################################################

# Provided by the postgresql-18-pgadmin-compat runtime package.
#
# pgAdmin uses version-specific entries in preference to the generic
# PostgreSQL entry.
DEFAULT_BINARY_PATHS = {
    "pg": "/usr/local/pgsql-18",
    "pg-18": "/usr/local/pgsql-18",
}


###############################################################################
# Session configuration
###############################################################################

SESSION_EXPIRATION_TIME = int(
    os.environ.get(
        "PGADMIN_SESSION_EXPIRATION_TIME",
        "1",
    )
)

##########################################################################
# Mail server settings
##########################################################################

MAIL_SERVER = os.getenv("PGADMIN_MAIL_SERVER", "localhost")
MAIL_PORT = int(os.getenv("PGADMIN_MAIL_PORT", "25"))
MAIL_USE_SSL = os.getenv("PGADMIN_MAIL_USE_SSL", "false").lower() == "true"
MAIL_USE_TLS = os.getenv("PGADMIN_MAIL_USE_TLS", "false").lower() == "true"
MAIL_USERNAME = os.getenv("PGADMIN_MAIL_USERNAME", "")
MAIL_PASSWORD = os.getenv("PGADMIN_MAIL_PASSWORD", "")

# Sender address should be configured by the deployment to match the
# SMTP provider's permitted sender/domain.
SECURITY_EMAIL_SENDER = os.getenv(
    "PGADMIN_SECURITY_EMAIL_SENDER",
    "no-reply@localhost",
)

###############################################################################
# Email validation
###############################################################################

CHECK_EMAIL_DELIVERABILITY = (
    os.environ.get(
        "PGADMIN_CHECK_EMAIL_DELIVERABILITY",
        "False",
    ).lower()
    == "true"
)

ALLOW_SPECIAL_EMAIL_DOMAINS = ast.literal_eval(
    os.environ.get(
        "PGADMIN_ALLOW_SPECIAL_EMAIL_DOMAINS",
        "[]",
    )
)

GLOBALLY_DELIVERABLE = (
    os.environ.get(
        "PGADMIN_GLOBALLY_DELIVERABLE",
        "True",
    ).lower()
    == "true"
)


###############################################################################
# Authentication
###############################################################################

AUTHENTICATION_SOURCES = ast.literal_eval(
    os.environ.get(
        "PGADMIN_AUTHENTICATION_SOURCES",
        "['internal']",
    )
)


###############################################################################
# OAuth2
###############################################################################

OAUTH2_CONFIG = [
    {
        "OAUTH2_NAME": os.environ.get(
            "PGADMIN_OAUTH2_NAME",
        ),
        "OAUTH2_DISPLAY_NAME": os.environ.get(
            "PGADMIN_OAUTH2_DISPLAY_NAME",
        ),
        "OAUTH2_CLIENT_ID": os.environ.get(
            "PGADMIN_OAUTH2_CLIENT_ID",
        ),
        "OAUTH2_CLIENT_SECRET": os.environ.get(
            "PGADMIN_OAUTH2_CLIENT_SECRET",
        ),
        "OAUTH2_TOKEN_URL": os.environ.get(
            "PGADMIN_OAUTH2_TOKEN_URL",
        ),
        "OAUTH2_AUTHORIZATION_URL": os.environ.get(
            "PGADMIN_OAUTH2_AUTHORIZATION_URL",
        ),
        "OAUTH2_USERINFO_ENDPOINT": os.environ.get(
            "PGADMIN_OAUTH2_USERINFO_ENDPOINT",
        ),
        "OAUTH2_SERVER_METADATA_URL": os.environ.get(
            "PGADMIN_OAUTH2_SERVER_METADATA_URL",
        ),
        "OAUTH2_SCOPE": os.environ.get(
            "PGADMIN_OAUTH2_SCOPE",
            "openid email profile",
        ),
        "OAUTH2_USERNAME_CLAIM": os.environ.get(
            "PGADMIN_OAUTH2_USERNAME_CLAIM",
        ),
        "OAUTH2_ICON": os.environ.get(
            "PGADMIN_OAUTH2_ICON",
            "fa-github",
        ),
        "OAUTH2_BUTTON_COLOR": os.environ.get(
            "PGADMIN_OAUTH2_BUTTON_COLOR",
        ),
        "OAUTH2_REDIRECT_URL": os.environ.get(
            "PGADMIN_OAUTH2_REDIRECT_URL",
        ),
        "OAUTH2_CHALLENGE_METHOD": os.environ.get(
            "PGADMIN_OAUTH2_CHALLENGE_METHOD",
            "S256",
        ),
        "OAUTH2_RESPONSE_TYPE": os.environ.get(
            "PGADMIN_OAUTH2_RESPONSE_TYPE",
            "code",
        ),
        "OAUTH2_CLIENT_AUTH_METHOD": os.environ.get(
            "PGADMIN_OAUTH2_CLIENT_AUTH_METHOD",
        ),
        "OAUTH2_WORKLOAD_IDENTITY_TOKEN_FILE": os.environ.get(
            "PGADMIN_OAUTH2_WORKLOAD_IDENTITY_TOKEN_FILE",
        ),
        "OAUTH2_API_BASE_URL": os.environ.get(
            "PGADMIN_OAUTH2_API_BASE_URL",
        ),
        "OAUTH2_ADDITIONAL_CLAIMS": os.environ.get(
            "PGADMIN_OAUTH2_ADDITIONAL_CLAIMS",
        ),
        "OAUTH2_SERVER_GROUP_CLAIM": os.environ.get(
            "PGADMIN_OAUTH2_SERVER_GROUP_CLAIM",
        ),
        "OAUTH2_SERVER_GROUP_CLAIM_MAPPING": ast.literal_eval(
            os.environ.get(
                "PGADMIN_OAUTH2_SERVER_GROUP_CLAIM_MAPPING",
                "None",
            )
        ),
        "OAUTH2_SSL_CERT_VERIFICATION": (
            os.environ.get(
                "PGADMIN_OAUTH2_SSL_CERT_VERIFICATION",
                "True",
            ).lower()
            == "true"
        ),
        "OAUTH2_LOGOUT_URL": os.environ.get(
            "PGADMIN_OAUTH2_LOGOUT_URL",
        ),
    }
]

OAUTH2_AUTO_CREATE_USER = (
    os.environ.get(
        "PGADMIN_OAUTH2_AUTO_CREATE_USER",
        "True",
    ).lower()
    == "true"
)

ENHANCED_COOKIE_PROTECTION = (
    os.environ.get(
        "PGADMIN_ENHANCED_COOKIE_PROTECTION",
        "False",
    ).lower()
    == "true"
)
