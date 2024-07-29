import os

import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import Client

# Load Firestore credentials from environment variable
cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

# Initialize Firebase app
firebase_admin.initialize_app(cred)

# Get a Firestore client
firestore_db: Client = firestore.client()
