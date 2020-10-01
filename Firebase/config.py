import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("YOUR_SECRET_KEY_HERE.json")
firebase = firebase_admin.initialize_app(cred)
db = firestore.client()
