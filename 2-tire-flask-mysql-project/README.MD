# Run the Project Manually with Docker
# Create a Custom Docker Network
docker network create techbase-net


# Build the Docker Images
docker build -t mysql:1.0.0 .
docker build -t flask:1.0.0 .

# Run the Containers
docker run -d --name my-mysql --network techbase-net -p 3306:3306 mysql:1.0.0
docker run -d --name flask-app --network techbase-net -p 5000:5000 flask:1.0.0