from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from passlib.hash import sha256_crypt

task = Blueprint("task", __name__)

