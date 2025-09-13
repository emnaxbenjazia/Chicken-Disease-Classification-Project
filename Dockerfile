# A Docker image is like a blueprint for your app:
# it contains the OS, Python, your code, and dependencies.
# When you run it, Docker creates a container (a lightweight isolated environment).

# we need to initialize some docker commands

FROM python:3.11-slim

# Install AWS CLI because we'll use S3
RUN apt-get update -y && apt-get install -y awscli && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy code in ./app inside the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your Flask app (replace app.py with main entrypoint if different)
CMD ["python3", "app.py"]
