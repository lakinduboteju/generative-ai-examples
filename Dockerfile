FROM python:3.12-slim

# Install Poetry
RUN pip install --no-cache-dir poetry~=1.8.3

# Configure Poetry not to create virtual environments
# then Poetry installs dependencies straight on the Docker container.
# As we run Python code on the Docker container, no need to have a virtual environment.
run poetry config virtualenvs.create false

# Install dependencies
copy src/pyproject.toml /app/pyproject.toml
workdir /app
run poetry install
run rm -f pyproject.toml poetry.lock
