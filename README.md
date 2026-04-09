# 🚀 Task Manager API

REST API for managing tasks in a kanban-style workflow, built with Flask. It allows creating projects, organizing tasks into columns (todo, in_progress, done), inviting collaborators, and tracking change history.

## 🛠️ Technologies

- **Python 3.10+**
- **Flask** — web framework
- **SQLAlchemy** — database ORM
- **SQLite** — database
- **JWT** — stateless authentication
- **bcrypt** — password hashing
- **Pydantic** — data validation and schemas
- **flask-openapi3** — automatic Swagger documentation

## ✨ Features

- JWT authentication with role-based access control (admin / user)
- Full CRUD for projects and tasks
- Kanban board with status (todo, in_progress, done) and priority (low, medium, high)
- Reordering and moving tasks between columns
- Project collaboration with member roles (viewer / editor)
- Filters by status, priority, and search by title
- Pagination for listings
- Task change history tracking
- Interactive documentation via Swagger

## 📂 Project Structure

```
app/
├── database/
│   ├── database.py       # SQLAlchemy instance
│   └── seeds.py          # admin user seed
├── routes/
│   ├── user_routes.py
│   ├── project_routes.py
│   ├── task_routes.py
│   └── member_routes.py
├── schemas/
│   ├── user_schemas.py
│   ├── project_schemas.py
│   ├── task_schemas.py
│   └── member_schemas.py
├── services/
│   ├── user_service.py
│   ├── project_service.py
│   ├── task_service.py
│   └── member_service.py
├── auth.py               # JWT and authentication decorators
├── models.py             # database models
└── __init__.py           # app factory
run.py
```

## ⚙️ Installation

**Prerequisites:** Python 3.10+ and pip

```bash
# Clone the repository
git clone https://github.com/prodsimu/flask-task-manager-api
cd flask-task-manager-api

# Install dependencies
pip install -e .

# Create environment variables file
cp .env.example .env
```

Edit the `.env` file with your secret key:

```env
SECRET_KEY=your-secret-key-here
```

## ▶️ Running the Project

```bash
python run.py
```

The server runs at `http://localhost:5000`. On the first run, the database is automatically created and an admin user is generated:

```
username: admin
password: admin123456
```

## 📄 Documentation

With the server running, access the interactive documentation:

```
http://localhost:5000/openapi/swagger
```

To authenticate in Swagger:
1. Use `POST /login` to obtain a token
2. Click **Authorize** and paste the token

## 🔌 Endpoints

### 🔐 Auth
| Method | Route | Description |
|--------|------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Authenticate and get a JWT token |

### 👤 Users
| Method | Route | Access | Description |
|--------|------|--------|-------------|
| GET | `/users` | admin | List users |
| POST | `/users` | admin | Create user |
| GET | `/profile` | authenticated | View own profile |
| PUT | `/profile/password` | authenticated | Change own password |
| PUT | `/users/<id>` | admin or self | Update user |
| DELETE | `/users/<id>` | admin | Delete user |

### 🗂️ Projects
| Method | Route | Access | Description |
|--------|------|--------|-------------|
| GET | `/projects` | authenticated | List projects |
| POST | `/projects` | authenticated | Create project |
| GET | `/projects/<id>` | member | View project |
| PUT | `/projects/<id>` | owner | Update project |
| DELETE | `/projects/<id>` | owner | Delete project |

### 📌 Tasks
| Method | Route | Access | Description |
|--------|------|--------|-------------|
| GET | `/projects/<id>/tasks` | member | List tasks |
| POST | `/projects/<id>/tasks` | editor | Create task |
| GET | `/projects/<id>/tasks/<id>` | member | View task |
| PUT | `/projects/<id>/tasks/<id>` | editor | Update task |
| PATCH | `/projects/<id>/tasks/<id>/move` | editor | Move task |
| DELETE | `/projects/<id>/tasks/<id>` | editor | Delete task |
| GET | `/projects/<id>/tasks/<id>/history` | member | View history |

### 👥 Members
| Method | Route | Access | Description |
|--------|------|--------|-------------|
| GET | `/projects/<id>/members` | member | List members |
| POST | `/projects/<id>/members` | owner | Add member |
| PUT | `/projects/<id>/members/<user_id>` | owner | Update role |
| DELETE | `/projects/<id>/members/<user_id>` | owner | Remove member |

## 🔍 Filters and Pagination

Listings accept query parameters:

```
GET /projects?page=1&per_page=10&search=marketing
GET /projects/<id>/tasks?status=todo&priority=high&search=bug&page=1&per_page=20
GET /users?page=1&per_page=10
```

All paginated responses follow this format:

```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "per_page": 10,
    "total": 43,
    "pages": 5
  }
}
```

## 🧩 Roles

### 👤 User roles
| Role | Description |
|------|-------------|
| `admin` | Full system access |
| `user` | Access to own resources |

### 👥 Project member roles
| Role | Description |
|------|-------------|
| `viewer` | View project and tasks |
| `editor` | Create, edit, and move tasks |

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Key used to sign JWT tokens | Yes |