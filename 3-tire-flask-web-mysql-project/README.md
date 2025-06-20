# 3-Tier Docker Architecture Project.

This project demonstrates a 3-tier architecture using Docker containers running on a Linux.  
It consists of three components, each in its own Docker container, connected via a custom Docker bridge network:

Frontend: Nginx web server serving static HTML form
Backend: Flask application processing form data
Database: MySQL storing submitted data

## Project Overview

- All containers communicate using a custom Docker network (`techbase-network`).
- Frontend serves HTML form and exposes port 80 to the host.
- Backend runs Flask app on port 5000 and connects to MySQL internally using container name.
- Form data submitted via frontend is sent to the backend and stored in MySQL.

## Step 1: Update Frontend with your publc IP

Edit the file:  frontend/index.html 
Change this line:

EX:
<form method="POST" action="http://192.168.71.130:5000/">
# OR
<form method="POST" action="http://your_IP:5000/">


## Step 2: Create Docker Network

docker network create techbase-network

## Step 3: Build Docker Images

docker build -t mysql:1.0.0 ./mysql
docker build -t backend:1.0.0 ./backend
docker build -t frontend:1.0.0 ./frontend

## Step 4: Run Containers
docker run -d --name my-mysql --network techbase-network mysql:1.0.0
docker run -d -p 5000:5000 --name my-backend --network techbase-network backend:1.0.0
docker run -d -p 80:80 --name my-frontend --network techbase-network frontend:1.0.0

## Access the Application

- Visit `http://<your-vm-ip>` in a browser to open the frontend form.
- Submitted data will be processed by Flask and saved to MySQL.


# Verify from the Database

docker exec -it my-mysql bash
mysql -u root -proot@123
show databases;
use Tech_Base_Hub_DB;
show tables;
SELECT * FROM submissions;

# Example Output

mysql> SELECT * FROM submissions;
+----+-----------------+--------------------------+
| id | name            | email                    |
+----+-----------------+--------------------------+
|  1 | Tummeti Krishna | krishnatummeti@gmail.com |
+----+-----------------+--------------------------+
1 row in set (0.00 sec)

mysql>
