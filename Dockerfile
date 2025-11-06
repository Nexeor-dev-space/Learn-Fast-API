# Use Python 3.12 as the base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy only dependency files first for caching
COPY pyproject.toml poetry.lock ./

# Install Poetry and project dependencies
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# Copy the entire project after dependencies are installed
COPY . .

# Make the start scripts executable
RUN chmod +x start.sh 

# Default to bash, command will be overridden by docker-compose
ENTRYPOINT ["/bin/bash"]