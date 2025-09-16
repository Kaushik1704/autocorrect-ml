# 🚀 Cloud-Deployed Autocorrect ML Model

A lightweight autocorrect ML model deployed on **AWS SageMaker (Free Tier)** as a REST API.  
Built in Python, containerized with Docker, pushed to **AWS ECR**, and served via **SageMaker real-time endpoint**.

---

## 🔹 Features
- Probabilistic autocorrect algorithm (edit distance + word frequency).
- Packaged in a Docker container with Flask + Gunicorn.
- Pushed to AWS ECR and deployed to SageMaker.
- Accessible via REST API:

POST /invocations
{ "word": "speling" }

Response:
{ "input": "speling", "suggestion": "spelling" }
