from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from passlib.hash import sha256_crypt

from models.user import User

auth = Blueprint("auth", __name__)

@auth.route("/auth/register", methods=["POST"])
def register():
    req = request.get_json()

    name = str(req["name"])
    lastname = str(req["lastname"])
    email = str(req["email"])
    password = str(req["password"])

    # Check if fields are empty

    if not name:
        return {"name": "This field is required."}, 400

    if not lastname:
        return {"lastname": "This field is required."}, 400

    if not email:
        return {"email": "This field is required."}, 400

    if not password:
        return {"password": "This field is required."}, 400

    existing_user = User.objects(email=email).first()
    
    if existing_user:
        return jsonify({"message": "Email is already in use."}), 422

    new_user = User.create(name=name, lastname=lastname, email=email, password=sha256_crypt.hash(password))
    #dict(new_user)
    #res = User.get(email=email)

    return {'message': 'OK'}, 201

@auth.route("/auth/login", methods=["POST"])
def login():
    req = request.get_json()

    email = str(req["email"])
    password_candidate = str(req["password"])

    if not email:
        return {"email": "This field is required."}, 400

    if not password_candidate:
        return {"password": "This field is required."}, 400

    existing_user = User.objects(email=email).first()

    if not existing_user:
        return jsonify({"message": "The email you entered is not connected to any account."}), 422

    if sha256_crypt.verify(password_candidate, existing_user.password):
        access_token = create_access_token(identity=existing_user.email)
        print("Access token:", access_token)
        resp = jsonify({'message': 'Uspešno prijavljivanje', 'access_token' : access_token})
        return resp, 200
    else:
        return jsonify({"message": "Wrong data"}), 422

@auth.route('/auth/current-user', methods=['GET'])
@jwt_required()
def current_user():
    user_id = get_jwt_identity()
    existing_user = User.objects(email=user_id).first()
    return jsonify(existing_user.serialize()), 200