# Let's start with a python 3.12 slim image
FROM python:3.12.2-slim

# Set the working directory in the container
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y gcc libffi-dev && rm -rf /var/lib/apt/lists/*

# Install Python Poetry with version 1.8.3
#RUN pip install poetry==1.8.3

COPY requirements.txt /app/

#RUN poetry install
RUN pip install -r requirements.txt

COPY . /app

# Run the application
#CMD ["poetry", "run", "python", "src/main.py"]
CMD ["python3", "src/main.py"]


