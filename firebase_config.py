import pyrebase4 as pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDg-R9gh6ASIERvKT2mvPEpdlxDKt-kh5s",
    "databaseURL": "https://dormbiz-5a339-default-rtdb.firebaseio.com/",
    "projectId": "dormbiz-5a339",
    "storageBucket": "your-app.appspot.com",
    "messagingSenderId": "541071685922",
    "appId": "1:541071685922:ios:1747693dcf5bfde10a0d7b"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

