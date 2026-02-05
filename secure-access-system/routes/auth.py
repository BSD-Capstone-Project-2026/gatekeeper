from flask import Blueprint, request, jsonify
from app import db
from models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()

    # 1️⃣ Validate input
    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not all([name, email, password, role]):
        return jsonify({"error": "All fields are required"}), 400

    # 2️⃣ Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 409

    # 3️⃣ Create user
    user = User(
        name=name,
        email=email,
        role=role
    )
    user.set_password(password)

    # 4️⃣ Save to DB
    db.session.add(user)
    db.session.commit()

    # 5️⃣ Response (safe)
    return jsonify({
        "message": "User registered successfully",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }), 201
