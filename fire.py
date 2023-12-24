import os

import firebase_admin
from firebase_admin import credentials

app = firebase_admin.initialize_app({
  "type": "service_account",
  "project_id": "notedown-by-dshaw0004",
  "private_key_id": os.getenv("KEYID"),
  "private_key": os.getenv("KEY"),
  "client_email": os.getenv("EMAIL"),
  "client_id": os.getenv("ID"),
  "auth_uri": os.getenv("AUTHURI"),
  "token_uri": os.getenv("TOKENURL"),
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.getenv("CERTURI"),
  "universe_domain": "googleapis.com"
}
)
