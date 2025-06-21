
# Flask + Redis Counter App (Without Docker Compose)

# Please fallow the steps


# Step 1: Build the Flask app image
docker build -t flask-app:1.0.0 .

# Optional: Verify the image is created
docker images

# Step 2: Create a custom Docker network
docker network create flask-app-network

# Optional: Inspect the network details
docker inspect flask-netwrok

# (Optional) You can pull the Redis image manually before running
docker pull redis:alpine

# Step 3: Run Redis container connected to the custom network
docker run -d --name redis --network flask-app-network redis:alpine


# Step 4: Run the Flask app container connected to the same network
docker run -d --name my-flask-app --network flask-app-network -p 5000:5000 flask-app:1.0.0

# Now you can check the application in your browser

# If running locally:
http://localhost:5000

# If running on a cloud server (like AWS EC2):
http://<your-ec2-public-ip>:5000

# Expected Output (in browser):
Hello, World! You have visited this page X times.


# once you connet you will see the count and also you can check this count in the Redis Container

docker exec -it redis sh

redis-cli

get hits

# Now you can see the output 




