# Use a generic and large base image
FROM python:latest
# Set the working directory
WORKDIR /app
# Copy dependency files
COPY requirements.txt ./
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the source code
COPY . .
# Run the app as the root user (bad practice)
USER root
# Default command
CMD ["python", "main.py"]