from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import current_app, request


def generate_token(user_id: int):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1),  # token válido 1 hora
    }
    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
    return token


def verify_token(token: str):
    try:
        payload = jwt.decode(
            token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
        )
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        raise ValueError("Token expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return {"error": "Token missing"}, 401

        # remove "Bearer " se existir
        if token.startswith("Bearer "):
            token = token[7:]

        try:
            user_id = verify_token(token)
        except ValueError as e:
            return {"error": str(e)}, 401

        return f(user_id=user_id, *args, **kwargs)

    return decorated
