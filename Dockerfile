# Use the latest official Python image as the base
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Create a non-root user named 'appuser' and switch to it
RUN useradd -m appuser
USER appuser

# Set the default command to run the application
CMD ["python", "main.py"]
