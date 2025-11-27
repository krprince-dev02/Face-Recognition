import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionattendanc-7c4fd-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "022":
        {
            "name": "Prince Kumar",
            "course": "MCA",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2023-06-05 20:37:34"
        },
    "011":
        {
            "name": "Akshay Kumar",
            "course": "MCA",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2023-06-05 20:37:34"
        },
    "033":
        {
            "name": "Sarvesh Sharma",
            "course": "MCA",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "A",
            "year": 1,
            "last_attendance_time": "2023-06-05 20:37:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)