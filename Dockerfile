# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire 'app' directory into the container
COPY app/ app/

# Command to run the Python script when the container starts
# This will be overridden by docker-compose for this specific project,
# but it's good practice to include a default.