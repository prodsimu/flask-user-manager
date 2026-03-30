from flask import Blueprint, jsonify, request

from app.auth import login_required
from app.services.project_service import ProjectService

project_bp = Blueprint("projects", __name__)
