# Use official Python image
FROM python:3.9-slim



RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
