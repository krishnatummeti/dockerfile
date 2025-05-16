# 3-Tier Docker Architecture Project on AWS EC2 (Free Tier)

This project demonstrates a simple 3-tier architecture using Docker containers running on a single AWS EC2 instance (t3.micro).  
It consists of three components, each running in its own Docker container, connected via a custom Docker bridge network:

- **Frontend:** Simple Nginx web server serving static HTML pages  
- **Backend:** Flask application providing REST API for data processing  
- **Database:** MySQL container storing data  

---

## Project Overview

- All three containers share a single Docker bridge network (`app-network`) to communicate internally.  
- The frontend container exposes port 80 to the EC2 instance for external access (web UI).  
- The backend connects to the MySQL database container internally using container name as hostname.  
- Data entered via the frontend is sent to the backend, which stores it in the MySQL database.

---

## Folder Structure

