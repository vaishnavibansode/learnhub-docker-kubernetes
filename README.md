# LearnHub — Docker and Kubernetes Deployment on AWS EC2

## Project Overview
LearnHub is a simple Flask-based online learning application containerized using Docker and deployed on Kubernetes on an AWS EC2 Ubuntu server.

## Technologies Used
- AWS EC2
- Ubuntu Server 24.04
- Python and Flask
- Docker
- Kubernetes
- Minikube
- kubectl
- Git and GitHub

## Application Features
- Displays sample online courses.
- Provides a `/health` endpoint.
- Runs inside a Docker container.
- Deployed using Kubernetes with two replicas.
- Exposed through a Kubernetes NodePort Service.

## Project Structure
- `app/app.py` — Flask application
- `requirements.txt` — Python dependencies
- `Dockerfile` — Docker image configuration
- `.dockerignore` — Files excluded from Docker build
- `deployment.yaml` — Kubernetes Deployment
- `service.yaml` — Kubernetes Service
- `screenshots/` — Implementation evidence

## Deployment Details
The Docker image `learnhub:1.0` is built on AWS EC2 and loaded into Minikube.

The Kubernetes Deployment maintains two application replicas. The Kubernetes Service exposes application port 5000 through Service port 80 and NodePort 30080.

## Verification
- Docker image built successfully.
- Docker container tested locally.
- Kubernetes node verified as Ready.
- Two LearnHub Pods verified as Running.
- Deployment verified with two available replicas.
- Kubernetes Service verified.
- Application health endpoint tested.

## Limitations
This is a demonstration application and not a complete Learning Management System. The project uses a single-node Minikube cluster hosted on AWS EC2.

## Security
Private keys, credentials, and access tokens must not be committed to this repository.
