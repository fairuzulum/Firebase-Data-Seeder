from firebase import get_firestore_client

def add_data_in_batch(data):
    db = get_firestore_client()
    batch = db.batch()

    for item in data:
        doc_ref = db.collection('Category').document()
        batch.set(doc_ref, item)

    try:
        batch.commit()
        print('Batch write successful')
    except Exception as e:
        print(f'Error writing batch: {e}')
