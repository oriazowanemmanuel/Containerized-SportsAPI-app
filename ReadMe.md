# 🏈 Sports API - NFL Schedule Flask App (Dockerized + AWS ECS)

This project is a simple Flask-based API that fetches the **NFL schedule** using [SerpAPI](https://serpapi.com/). It's containerized with Docker, deployed to AWS ECS, and made publicly accessible via API Gateway.

---

Full Article link: https://emmanueloriazowan.hashnode.dev/building-a-sports-api-with-flask-application-load-balancer-and-aws-ecs-a-full-guide#heading-architecture

## 🚀 Features

- Returns live NFL schedule data
- Built with Flask and Python
- Containerized using Docker
- Deployed using AWS ECS (Fargate)
- Connected to API Gateway for public access

---

## 🛠️ Tech Stack

- **Flask** (Python Web Framework)
- **Docker** (Containerization)
- **Amazon ECR** (Container Registry)
- **Amazon ECS Fargate** (Container Orchestration)
- **API Gateway** (Public API exposure)
- **SerpAPI** (Data source for sports schedules)

---

## 📦 Installation (Local)

1. **Clone the repo**
   ```bash
   git clone https://github.com/oriazowanemmanuel/Containerized-SportsAPI-app.git

2. # In .env file or export manually
SPORTS_API_KEY=your_serpapi_key

3. #pip install -r requirements.txt

4. #Run the app
 python3 app.py

5. #Build the image

docker build -t sports-api .

6.Build and deploy to ECR

docker build --platform linux/amd64 -t sports-api .
docker tag sports-api:latest <AWS_ACCOUNT_ID>.dkr.ecr.<region>.amazonaws.com/sports-api:sports-api-latest
docker push <AWS_ACCOUNT_ID>.dkr.ecr.<region>.amazonaws.com/sports-api:sports-api-latest

7. Login to AWS to confirm the image was properly pushed to ECR
8. Login to ECS to create a task and then a service from the image uploaded to the ECR
9. COnfigure a loadbalancer to sit in front of the container cluster
9. Test with the container endpoint
10. Configure an API gateway to sit in front of the loadbalancer and send get requests
11. Test again using the API gateway endpoint

See the full documentation on: https://emmanueloriazowan.hashnode.dev/building-a-sports-api-with-flask-application-load-balancer-and-aws-ecs-a-full-guide#heading-architecture

