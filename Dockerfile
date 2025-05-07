# Container image that runs your code
FROM --platform=linux/amd64 python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY main.py /app/

# Make the script executable
RUN chmod +x /app/main.py

# Set the entrypoint
ENTRYPOINT ["python3", "/app/main.py"]

# Default command (can be overridden by args)
CMD []
