import firebase_admin
from firebase_admin import credentials, firestore

# Inisialisasi dengan kunci layanan
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Mendapatkan referensi ke Firestore
db = firestore.client()

def get_firestore_client():
    return db
