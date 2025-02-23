<<<<<<< HEAD
# AI-voice-assistant
Build a Simple AI Voice Assistant (Backend Requirements)
=======
# AI Voice Assistant

## Overview

This project is an AI-powered voice assistant built using FastAPI. It processes voice and text inputs and provides intelligent responses. The application is containerized with Docker and deployed on Kubernetes using Minikube.

## Features

- Voice and text input processing
- RESTful API built with FastAPI
- Dockerized for easy deployment
- Kubernetes deployment with Minikube

## Prerequisites

Ensure you have the following installed:

- Python 3.9+
- Docker & Docker Compose
- Minikube & kubectl

## Project Structure

```
AI Virtual Agent/
├── app/
│   ├── main.py          # FastAPI application
│   ├── logging_config.py        
│   ├── nlp_processing.py      
│   ├── utils.py         # Helper functions
│
├── Dockerfile           # Docker container configuration
├── requirements.txt     # Python dependencies
├── kubernetes/
│   ├── deployment.yaml      # Kubernetes Deployment & Service
│
├── README.md            # Documentation
```

## Setup

1. Clone the Repository
    ```bash
    git clone https://github.com/yourusername/ai-voice-assistant.git
    cd ai-voice-assistant
    ```

2. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Run Locally
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

4. Test API
    Open in a browser:
    ```
    http://127.0.0.1:8000/docs
    ```
    Or use CURL:
    ```bash
    curl -X POST "http://127.0.0.1:8000/process-text/" -H "Content-Type: application/json" -d '{"text": "Hello"}'
    ```

## Docker Deployment

1. Build and Run Docker Container
    ```bash
    docker build -t ai-virtual-agent .
    docker run -d -p 8000:8000 --name ai-agent ai-virtual-agent
    ```

## Kubernetes Deployment with Minikube

1. Start Minikube
    ```bash
    minikube start
    ```

2. Deploy to Kubernetes
    ```bash
    kubectl apply -f kubernetes/deploy.yaml
    ```

3. Get Minikube IP
    ```bash
    minikube ip
    ```

4. Access API
    Replace `<MINIKUBE_IP>` with the actual Minikube IP:
    ```bash
    curl -X POST "http://<MINIKUBE_IP>:30007/process-text/" -H "Content-Type: application/json" -d '{"text": "Hello"}'
    ```

## Troubleshooting

- If Docker conflicts, remove the existing container:
    ```bash
    docker rm -f ai-agent
    ```

- If Kubernetes service is not reachable, check pod logs:
    ```bash
    kubectl logs <pod-name>
    ```
>>>>>>> 6ba8f26 (Initial commit: Added AI Voice Assistant with Kubernetes deployment)
