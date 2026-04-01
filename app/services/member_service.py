from app.database.database import db
from app.models import MemberRole, Project, ProjectMember, User


class MemberService:

    @staticmethod
    def _get_project_as_owner(project_id: int, owner_id: int):
        project = db.session.get(Project, project_id)

        if not project:
            raise ValueError("Project not found.")

        if project.owner_id != owner_id:
            raise PermissionError("Only the project owner can manage members.")

        return project
