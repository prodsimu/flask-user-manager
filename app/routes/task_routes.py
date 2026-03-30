from flask import Blueprint, jsonify, request

from app.auth import login_required
from app.services.task_service import TaskService

task_bp = Blueprint("tasks", __name__)
