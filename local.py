from google.oauth2.service_account import Credentials
from app import main
import logging

logging.getLogger().setLevel(logging.INFO)

key_path = '/app/gcp-service-key.json'
credentials = Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

app, server = main(credentials)