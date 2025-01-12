# Use an official Python image as a base
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose a port if necessary (e.g., for a web application)
# EXPOSE 8000

# Set the entry point
CMD ["python", "main.py"]