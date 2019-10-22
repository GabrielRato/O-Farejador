from flask import Flask
import json
import pyrebase



app = Flask(__name__)

@app.route("/")
def hello():
    config = {
      "apiKey": " AIzaSyB4roWNLB_7MItUHCKyZ2XPLo-l9AM7ogY ",
      "authDomain": "respirafundo-1bb3f.firebaseapp.com",
      "databaseURL": "https://respirafundo-1bb3f.firebaseio.com",
      "storageBucket": "respirafundo-1bb3f.appspot.com",
      "serviceAccount": "serviceAccountCredentials.json"
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    data = db.child("RespiraFundo").get()
    print(data.val()) # {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}

    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":

    app.run(host='0.0.0.0', debug=True)
