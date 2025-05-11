# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Set environment variable for Flask
ENV FLASK_ENV=development

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["python", "app.py"]
