from random import randint
from datetime import datetime

from firebase_admin import firestore

from fire import app

db = firestore.client(app)


def get_all_message():
    ref = db.collection("messages")
    docs = ref.stream()
    all_todo = []
    for doc in docs:
        #        print(f"{doc.id} => {doc.to_dict()}")
        all_todo.append(doc.to_dict())
#    print(all_messages)
    return all_todo


def add_new_message(title: str, desc: str, extra: object = {}):

    no_of_message = randint(1, 99999) * randint(5, 77635)
    doc_ref = db.collection("messages").document(f"devp{no_of_message}")
    doc_ref.set({"title": title, "description": desc, "isCompleted": False, "creationDate": datetime.now(),
                "extraStuff": extra})
