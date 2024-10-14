
# Let's start with a python 3.10 slim image
FROM python:3.12.2-slim

# Set the working directory in the container
WORKDIR /app

# Install Python Poetry with version 1.8.3
RUN pip install poetry==1.8.3

COPY pyproject.toml poetry.lock /app/

RUN poetry install

COPY . /app

# Run the application
CMD ["poetry", "run", "python", "src/main.py"]
