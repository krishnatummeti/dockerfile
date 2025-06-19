
# Flask + Redis Counter App (Without Docker Compose)

# Please fallow the steps


# Step 1: Build the Flask app image
docker build -t flask-app .

# Optional: Verify the image is created
docker images

# Step 2: Create a custom Docker network
docker network create flask-netwrok

# Optional: Inspect the network details
docker inspect flask-netwrok

# (Optional) You can pull the Redis image manually before running
docker pull redis:alpine

# Step 3: Run Redis container connected to the custom network
docker run -d --name redis --network flask-netwrok redis:alpine


# Step 4: Run the Flask app container connected to the same network
docker run -d --name my-flask-app --network flask-netwrok -p 5000:5000 flask-app

# Now you can check the application in your browser

# If running locally:
http://localhost:5000

# If running on a cloud server (like AWS EC2):
http://<your-ec2-public-ip>:5000

# Expected Output (in browser):
Hello, World! You have visited this page X times.



