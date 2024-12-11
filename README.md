# Distributed Multi-tier Web Application with Docker, Kubernetes, and GitHub

## Project Overview

This project is a web application that demonstrates the integration of a React frontend, a Flask backend, and a database. The entire application is containerized using Docker, deployed to a Kubernetes cluster, and version-controlled with GitHub. The frontend communicates with the backend through REST APIs, and the backend connects to a database for data storage.

### Features:
- **Frontend**: A React application that captures user input and sends it to the backend via HTTP requests.
- **Backend**: A Python Flask application that processes the input data, connects to a database, and returns responses.
- **Database**: A simple database for storing user-submitted data (e.g., MySQL, PostgreSQL).
- **Docker**: Each component (frontend, backend, database) is containerized using Docker.
- **Kubernetes**: The application is deployed to Google Kubernetes Engine (GKE) for orchestration.
- **Monitoring and Logging**: Basic monitoring and logging for the Kubernetes cluster using Google Cloud Operations.

---

## Table of Contents
1. [Project Architecture](#project-architecture)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Local Development](#local-development)
    - [Docker Setup](#docker-setup)
    - [Kubernetes Setup](#kubernetes-setup)
4. [Version Control](#version-control)
5. [Deployment](#deployment)
6. [Challenges and Solutions](#challenges-and-solutions)

---

## Project Architecture

- **Frontend (React)**: A form that captures user input.
- **Backend (Flask)**: An API to process the data and store it in the database.
- **Database**: A persistent data store for saving user inputs.
- **Docker & Kubernetes**: The whole project is containerized and orchestrated using Kubernetes on Google Kubernetes Engine (GKE).

---

## Technologies Used

- **Frontend**: ReactJS, HTML, CSS
- **Backend**: Flask (Python)
- **Database**: MySQL/PostgreSQL
- **Containerization**: Docker
- **Orchestration**: Kubernetes (GKE)
- **Version Control**: GitHub
- **Monitoring/Logging**: Google Cloud Operations (Stackdriver)

---

## Setup Instructions

### Prerequisites

Make sure you have the following installed:
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Kubectl**: [Install Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- **Google Cloud SDK**: [Install Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- **Git**: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Local Development

#### Frontend
1. Navigate to the `frontend/` directory.
2. Install dependencies:
    ```bash
    npm install
    ```
3. Start the development server:
    ```bash
    npm start
    ```
4. The app will run at `http://localhost:3000`.

#### Backend
1. Navigate to the `backend/` directory.
2. Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3. Start the Flask server:
    ```bash
    flask run
    ```
4. The backend will run at `http://localhost:8082`.

### Docker Setup

#### Frontend Dockerization
1. Navigate to the `frontend/` directory.
2. Build the Docker image:
    ```bash
    docker build -t frontend .
    ```
3. Run the container:
    ```bash
    docker run -p 3000:80 frontend
    ```

#### Backend Dockerization
1. Navigate to the `backend/` directory.
2. Build the Docker image:
    ```bash
    docker build -t backend .
    ```
3. Run the container:
    ```bash
    docker run -p 8082:8082 backend
    ```

### Kubernetes Setup

1. Push Docker images to Google Container Registry (GCR):
    ```bash
    docker tag frontend gcr.io/[PROJECT_ID]/frontend:v1
    docker push gcr.io/[PROJECT_ID]/frontend:v1

    docker tag backend gcr.io/[PROJECT_ID]/backend:v1
    docker push gcr.io/[PROJECT_ID]/backend:v1
    ```

2. Apply Kubernetes configuration:
    ```bash
    kubectl apply -f frontend/deployment.yaml
    kubectl apply -f backend/deployment.yaml
    ```

3. Verify deployments:
    ```bash
    kubectl get pods
    kubectl get svc
    ```

4. Access the frontend via the external IP of the frontend service.

---

## Version Control

This project follows best practices for version control using GitHub.

- **Branches**:
  - `main`: Stable branch with production-ready code.
  - `feature/[feature-name]`: For developing new features.
  - `fix/[bug-name]`: For bug fixes.
  
- **Pull Requests**: Each feature or bugfix is merged into the `main` branch using pull requests. Conflicts are resolved before merging.

---

## Deployment

The application is deployed on **Google Kubernetes Engine (GKE)**. Each service (frontend and backend) runs in its own pod, and the frontend is accessible through a LoadBalancer service.

---

## Challenges and Solutions

### 1. **Environment Variables**:
Managing environment variables across Docker and Kubernetes was tricky, especially ensuring that the frontend could dynamically access the backend URL.
- **Solution**: I used Kubernetes config maps and secrets to inject environment variables into the pods during deployment.

### 2. **Containerization**:
Optimizing Dockerfiles for both the frontend and backend was a challenge, as the initial images were too large.
- **Solution**: I used multi-stage builds in the Dockerfiles to reduce image size, especially for the frontend.

### 3. **Kubernetes Networking**:
Ensuring the backend could communicate with the database in the Kubernetes cluster required running cloud sql proxy container side by side with project.
- **Solution**: I deployed the `cloud sql proxy` container alongside the `backend project container`. 

---

## Conclusion

This project demonstrates how to build, containerize, and deploy a full-stack web application using modern tools like Docker, Kubernetes, and GitHub. By following best practices for containerization, orchestration, and version control, I was able to develop and manage a scalable application with ease.

