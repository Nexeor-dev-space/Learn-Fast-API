FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

# Copy only pyproject.toml first (no poetry.lock)
COPY pyproject.toml ./

# Install dependencies without lock file
RUN poetry config virtualenvs.create false && poetry install --no-root

# Now copy the rest of the application
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]