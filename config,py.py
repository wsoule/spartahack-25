import firebase_admin
from firebase_admin import credentials, auth
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/your/firebase/service/account/key.json")
firebase_admin.initialize_app(cred)

@app.route('/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    password = request.json.get('password')

    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        return jsonify({"message": "User created successfully", "user_id": user.uid})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        id_token = user['idToken']
        return jsonify({"id_token": id_token})
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@app.route('/protected', methods=['GET'])
def protected():
    id_token = request.headers.get('Authorization')

    if not id_token:
        return jsonify({"error": "Unauthorized"}), 401

    try:
        decoded_token = auth.verify_id_token(id_token)
        user_id = decoded_token['uid']
        # Fetch user data from your database based on user_id
        return jsonify({"message": "Protected route accessed", "user_id": user_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 401

if __name__ == '__main__':
    app.run(debug=True)