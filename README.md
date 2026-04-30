# 🏋️ Gym Management Application

## 📌 Overview

A Flask-based web application designed to manage gym members, integrated with a complete CI/CD pipeline using GitHub Actions and Jenkins.

This project demonstrates modern DevOps practices including automated testing, containerization, and continuous integration.

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** SQLite
* **ORM:** Flask-SQLAlchemy
* **Testing:** Pytest
* **Containerization:** Docker
* **CI/CD:** GitHub Actions, Jenkins

---

# ⚙️ Local Setup & Execution

## 🔹 1. Clone the Repository

```bash
git clone https://github.com/Vin81-lab/gym-app.git
cd gym-app
```

---

## 🔹 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔹 4. Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 🧪 Running Tests Manually

## 🔹 Run Tests Locally

```bash
pytest
```

---

## 🔹 Run Tests Inside Docker

Build the Docker image:

```bash
docker build -t gym-app .
```

Run tests inside container:

```bash
docker run -e PYTHONPATH=/app gym-app pytest
```

---

# 🔄 CI/CD Pipeline Overview

## 🔹 GitHub Actions (Primary CI)

Triggered on:

* Push to `main`
* Pull Request to `main`

### Pipeline Steps:

1. **Checkout Code**
2. **Linting**

   * Uses `flake8` to enforce code quality
3. **Build Docker Image**

   * Ensures application builds successfully
4. **Run Tests Inside Container**

   * Executes `pytest` in Docker environment

👉 Ensures code quality before merge

---

## 🔹 Jenkins (Secondary Build & Quality Gate)

Jenkins is configured as a pipeline job using a `Jenkinsfile`.

### Responsibilities:

* Pull latest code from GitHub
* Create a clean Python environment
* Install dependencies
* Run test suite
* Build Docker image

👉 Acts as an additional validation layer for builds

---

## 🔹 Webhook Integration

* GitHub sends webhook events on code push
* Jenkins is exposed using **ngrok**
* Webhook triggers Jenkins pipeline automatically

---

# 🔁 CI/CD Workflow

The pipeline is triggered on every push and pull request.

Stages:
1. Lint & Build
2. Run Tests
3. SonarCloud Analysis (Code Quality)
4. Docker Image Build & Push
5. Deploy to Kubernetes (GKE)
---

# 🎯 Key Highlights

* Automated CI pipeline using GitHub Actions
* Containerized testing using Docker
* Jenkins integration as a secondary quality gate
* Webhook-based automation for build triggering

---

# 👨‍💻 Author

Vinod Muraleedharan

---

# 📄 License

This project is for educational and demonstration purposes.

## 🏗️ Architecture Diagram

        Developer (Git Push)
                │
                ▼
        GitHub Repository
                │
                ▼
        GitHub Actions (CI/CD Pipeline)
        ┌───────────────────────────────┐
        │ 1. Lint & Build              │
        │ 2. Run Tests                 │
        │ 3. SonarCloud Analysis 📊    │
        │    - Code Quality            │
        │    - Quality Gate            │
        └───────────────────────────────┘
                │
                ▼
        Docker Build & Push
                │
                ▼
        Docker Hub (Image Registry)
                │
                ▼
        Google Kubernetes Engine (GKE)
        ┌───────────────────────────────┐
        │ Deployment (Pods)            │
        │ Service (LoadBalancer)       │
        └───────────────────────────────┘
                │
                ▼
        Public URL (External IP)
                │
                ▼
           End Users 🌐


#Test CI?CD pipeline

#Tech Stack

- Python (Flask)
- Docker
- Kubernetes (GKE)
- GitHub Actions
- Docker Hub
- Google Cloud Platform

# Kubernetes depoyment

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# CI/CD pipeline

- Trigger: push / pull_request
- Build Docker image
- Push to Docker Hub
- Deploy to GKE automatically

# Live application

http://34.14.212.173:5000/members

## Code Quality (SonarCloud)

This project integrates SonarCloud for continuous code quality analysis.

Features:
- Static code analysis
- Detection of bugs, vulnerabilities, and code smells
- Maintainability and reliability ratings
- Quality Gate enforcement (build fails if standards are not met)

Dashboard:
https://sonarcloud.io/project/overview?id=Vin81-lab_gym-app


