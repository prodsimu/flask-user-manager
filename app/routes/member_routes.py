from flask import Blueprint, jsonify, request

from app.auth import login_required
from app.services.member_service import MemberService

member_bp = Blueprint("members", __name__)


# GET

# POST


@member_bp.route("/projects/<int:project_id>/members", methods=["POST"])
@login_required
def add_member(user_id, project_id):
    data = request.get_json()

    try:
        member = MemberService.add_member(
            project_id=project_id,
            owner_id=user_id,
            username=data.get("username"),
            role=data.get("role", "viewer"),
        )
        return (
            jsonify(
                {
                    "id": member.id,
                    "user_id": member.user_id,
                    "username": member.user.username,
                    "role": member.role,
                    "joined_at": member.joined_at.isoformat(),
                }
            ),
            201,
        )

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except PermissionError as e:
        return jsonify({"error": str(e)}), 403


# PUT

# DELETE
