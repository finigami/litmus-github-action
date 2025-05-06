# Container image that runs your code
FROM --platform=linux/amd64 python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Python script
COPY main.py /app/

# Make the script executable
RUN chmod +x /app/main.py

# Set the entrypoint
ENTRYPOINT ["python3", "/app/main.py"]
