import ast
import builtins
import os
import sys

UTILS_DIR = "/usr/lib/pgadmin4/pgadmin/utils"
if UTILS_DIR not in sys.path:
    sys.path.insert(0, UTILS_DIR)

from pgadmin.utils.check_external_config_db import check_external_config_db
from pgadmin.utils.validation_utils import validate_email

builtins.SERVER_MODE = True


def external_config_db_exists():
    raw = os.environ.get("PGADMIN_CONFIG_CONFIG_DATABASE_URI")

    if not raw:
        return False

    try:
        uri = ast.literal_eval(raw)
    except (ValueError, SyntaxError):
        uri = raw

    try:
        return check_external_config_db(uri)
    except Exception:
        return False


external_db_exists = external_config_db_exists()

if not os.path.isfile("/var/lib/pgadmin/pgadmin4.db") and not external_db_exists:
    email = os.environ.get("PGADMIN_SETUP_EMAIL")
    password = os.environ.get("PGADMIN_SETUP_PASSWORD")

    if not email or not password:
        raise RuntimeError(
            "You need to define PGADMIN_SETUP_EMAIL and PGADMIN_SETUP_PASSWORD."
        )

    check_email_deliverability = (
        os.environ.get(
            "PGADMIN_CHECK_EMAIL_DELIVERABILITY",
            "False",
        ).lower()
        == "true"
    )

    allow_special_email_domains = ast.literal_eval(
        os.environ.get(
            "PGADMIN_ALLOW_SPECIAL_EMAIL_DOMAINS",
            "[]",
        )
    )

    globally_deliverable = (
        os.environ.get(
            "PGADMIN_GLOBALLY_DELIVERABLE",
            "True",
        ).lower()
        == "true"
    )

    email_config = {
        "CHECK_EMAIL_DELIVERABILITY": check_email_deliverability,
        "ALLOW_SPECIAL_EMAIL_DOMAINS": allow_special_email_domains,
        "GLOBALLY_DELIVERABLE": globally_deliverable,
    }

    if not validate_email(email, email_config):
        raise RuntimeError(f"'{email}' does not appear to be a valid email address.")


from pgAdmin4 import app
