# 📝 FastAPI ToDo Backend

A modern, async-first backend ToDo API using:

- FastAPI
- SQLAlchemy (Async)
- PostgreSQL
- JWT Authentication
- Alembic for Migrations
- Poetry for Dependency Management

---

## 🚀 Project Setup

### 📦 Requirements

- Python 3.11+
- PostgreSQL
- Poetry (`pip install poetry`)

### 📁 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/fastapi-todo.git
   cd fastapi-todo
   ```
2. Install dependencies:
   - Install poetry
      - CMD, PowerShell, Git Bash, or Windows Terminal:
         ```bash
         (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
         ```
      - Linux/macOS:
         ```bash
         curl -sSL https://install.python-poetry.org | python3 -
         ```
   - Add Poetry to PATH (Windows only)
   - Verify
      ```bash
      poetry --version
      ``` 
   - Install Packages
      ```bash
      poetry install
      ```  

3. Create database:
   1. Install `postgresql` in your machine
      - Windows:
         - Go to:👉 https://www.postgresql.org/download/windows/
         - Click "Download the installer" → Choose Windows x86-64.
         - Add `psql` to your `PATH`. Usually: `C:\Program Files\PostgreSQL\<version>\bin`
         - ![image](https://github.com/user-attachments/assets/2dc2d80d-4605-49cf-9709-801ebcd42dcb)

      - Mac:
         ```bash
         brew install postgresql@16
         brew services start postgresql@16
         ```
      - Debian:
         ```bash
         sudo apt update
         sudo apt install postgresql postgresql-contrib
         ```
   2. Verify installation.
      ```bash
      psql -U postgres
      ```
   3. Create User and DB.
      ```sql
      -- Create a user
      CREATE USER todo_user WITH PASSWORD 'todo_pass';

      -- Create database
      CREATE DATABASE todo_db OWNER todo_user;
    
      -- Grant privileges
      GRANT ALL PRIVILEGES ON DATABASE todo_db TO todo_user;

      \q  -- exit
      ```
      **Note**: Replace todo_user, todo_pass, todo_db with appropriate names
4. Set environment variables in .env:
```ini
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/todo_db
JWT_SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_MINUTES=10080
JWT_ALGORITHM=HS256
```

5. Apply migrations:
```bash
alembic upgrade head
```
6. Run the server:
   - Fastapi app is deployed by:
      ```bash
      poetry run uvicorn app.main:app --reload
      ```
   - However since we are dockerizing the project, the whole deploy command is in docker compose.

### 👥 Developer Workflow

To ensure clear code tracking and review:

1. Start from the main branch:
   ```bash
   git checkout main
   ```
2. Create your personal branch:
   ```bash
   git checkout -b main_<your_username>
   ```
3. Pick an issue from the GitHub Issues board.
4. Commit progress regularly:
   ```bash
   git add .
   git commit -m "✅ Implemented user registration"
   git push origin main_<your_username>
   ```
5. When a task is complete, mark the GitHub issue and notify for review.

### 🛠️ Common FastAPI Commands

| Action                        | Command                                     |
| ----------------------------- | ------------------------------------------- |
| Start development server      | `poetry run uvicorn app.main:app --reload`  |
| Generate new Alembic revision | `alembic revision --autogenerate -m "desc"` |
| Apply DB migrations           | `alembic upgrade head`                      |
| Revert last migration         | `alembic downgrade -1`                      |

### 📚 References

- 📘 [FastAPI](https://fastapi.tiangolo.com/)
- 📘 [Pydantic (v2)](https://docs.pydantic.dev/2.9/)
- 📘 [SQLAlchemy (Async)](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
- 📘 [Alembic](https://alembic.sqlalchemy.org/en/latest/)

### 📂Directory Layout

```
app/
├── main.py          # FastAPI app entry point
├── core/            # Settings, auth utils
├── db/              # DB connection and session
├── models/          # SQLAlchemy ORM models
├── schemas/         # Pydantic request/response models
├── routes/          # API route handlers
├── services/        # Business logic

```

