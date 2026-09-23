import ast
import os


###############################################################################
# Wolfi distribution / filesystem configuration
###############################################################################

# System CA bundle provided by Wolfi's ca-certificates package.
CA_FILE = os.environ.get(
    'PGADMIN_CA_FILE',
    '/etc/ssl/certs/ca-certificates.crt',
)

# Do not write application logs into the image filesystem.
LOG_FILE = '/dev/null'

# Documentation is installed as a sibling of the pgAdmin application
# directory:
#
#   /usr/lib/pgadmin4/
#   /usr/lib/pgadmin4/docs/
#
HELP_PATH = '../../docs'

# This is a web/server deployment, not the desktop runtime.
SERVER_MODE = True


###############################################################################
# PostgreSQL client binaries
###############################################################################

# Provided by the postgresql-18-pgadmin-compat runtime package.
#
# pgAdmin uses version-specific entries in preference to the generic
# PostgreSQL entry.
DEFAULT_BINARY_PATHS = {
    'pg': '/usr/local/pgsql-18',
    'pg-18': '/usr/local/pgsql-18',
}


###############################################################################
# Session configuration
###############################################################################

SESSION_EXPIRATION_TIME = int(
    os.environ.get(
        'PGADMIN_SESSION_EXPIRATION_TIME',
        '7',
    )
)


###############################################################################
# Email validation
###############################################################################

CHECK_EMAIL_DELIVERABILITY = (
    os.environ.get(
        'PGADMIN_CHECK_EMAIL_DELIVERABILITY',
        'False',
    ).lower() == 'true'
)

GLOBALLY_DELIVERABLE = (
    os.environ.get(
        'PGADMIN_GLOBALLY_DELIVERABLE',
        'True',
    ).lower() == 'true'
)

ALLOW_SPECIAL_EMAIL_DOMAINS = ast.literal_eval(
    os.environ.get(
        'PGADMIN_ALLOW_SPECIAL_EMAIL_DOMAINS',
        '[]',
    )
)


###############################################################################
# Authentication
###############################################################################

AUTHENTICATION_SOURCES = ast.literal_eval(
    os.environ.get(
        'PGADMIN_AUTHENTICATION_SOURCES',
        "['oauth2']",
    )
)

MASTER_PASSWORD_REQUIRED = (
    os.environ.get(
        'PGADMIN_MASTER_PASSWORD_REQUIRED',
        'True',
    ).lower() == 'true'
)


###############################################################################
# OAuth2
###############################################################################

OAUTH2_CONFIG = [{
    'OAUTH2_NAME': os.environ.get(
        'PGADMIN_OAUTH2_NAME',
    ),

    'OAUTH2_DISPLAY_NAME': os.environ.get(
        'PGADMIN_OAUTH2_DISPLAY_NAME',
    ),

    'OAUTH2_CLIENT_ID': os.environ.get(
        'PGADMIN_OAUTH2_CLIENT_ID',
    ),

    'OAUTH2_CLIENT_SECRET': os.environ.get(
        'PGADMIN_OAUTH2_CLIENT_SECRET',
    ),

    'OAUTH2_TOKEN_URL': os.environ.get(
        'PGADMIN_OAUTH2_TOKEN_URL',
    ),

    'OAUTH2_AUTHORIZATION_URL': os.environ.get(
        'PGADMIN_OAUTH2_AUTHORIZATION_URL',
    ),

    'OAUTH2_USERINFO_ENDPOINT': os.environ.get(
        'PGADMIN_OAUTH2_USERINFO_ENDPOINT',
    ),

    'OAUTH2_SERVER_METADATA_URL': os.environ.get(
        'PGADMIN_OAUTH2_SERVER_METADATA_URL',
    ),

    'OAUTH2_SCOPE': os.environ.get(
        'PGADMIN_OAUTH2_SCOPE',
        'openid email profile',
    ),

    'OAUTH2_USERNAME_CLAIM': os.environ.get(
        'PGADMIN_OAUTH2_USERNAME_CLAIM',
    ),

    'OAUTH2_ICON': os.environ.get(
        'PGADMIN_OAUTH2_ICON',
        'fa-github',
    ),

    'OAUTH2_BUTTON_COLOR': os.environ.get(
        'PGADMIN_OAUTH2_BUTTON_COLOR',
    ),

    'OAUTH2_REDIRECT_URL': os.environ.get(
        'PGADMIN_OAUTH2_REDIRECT_URL',
    ),

    'OAUTH2_CHALLENGE_METHOD': os.environ.get(
        'PGADMIN_OAUTH2_CHALLENGE_METHOD',
        'S256',
    ),

    'OAUTH2_RESPONSE_TYPE': os.environ.get(
        'PGADMIN_OAUTH2_RESPONSE_TYPE',
        'code',
    ),

    'OAUTH2_CLIENT_AUTH_METHOD': os.environ.get(
        'PGADMIN_OAUTH2_CLIENT_AUTH_METHOD',
    ),

    'OAUTH2_WORKLOAD_IDENTITY_TOKEN_FILE': os.environ.get(
        'PGADMIN_OAUTH2_WORKLOAD_IDENTITY_TOKEN_FILE',
    ),

    'OAUTH2_API_BASE_URL': os.environ.get(
        'PGADMIN_OAUTH2_API_BASE_URL',
    ),

    'OAUTH2_ADDITIONAL_CLAIMS': os.environ.get(
        'PGADMIN_OAUTH2_ADDITIONAL_CLAIMS',
    ),

    'OAUTH2_SSL_CERT_VERIFICATION': (
        os.environ.get(
            'PGADMIN_OAUTH2_SSL_CERT_VERIFICATION',
            'True',
        ).lower() == 'true'
    ),

    'OAUTH2_LOGOUT_URL': os.environ.get(
        'PGADMIN_OAUTH2_LOGOUT_URL',
    ),
}]
