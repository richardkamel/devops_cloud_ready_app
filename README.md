# \# DevOps Cloud-Ready Application

# 

# This project demonstrates core DevOps concepts through a small cloud-ready web application.

# The goal is to simulate a production-like environment using containerization, service orchestration, monitoring, and continuous integration.

# 

# The application is intentionally simple in terms of business logic in order to focus on infrastructure, automation, and observability.

# 

# ---

# 

# \## Project Overview

# 

# The project consists of a REST API built with FastAPI, packaged into a Docker container and orchestrated using Docker Compose.

# The application is monitored using Prometheus and Grafana, and its quality is enforced through an automated CI pipeline using GitHub Actions.

# 

# This project was built as a personal DevOps learning project to gain hands-on experience with modern DevOps tools and workflows.

# 

# ---

# 

# \## Architecture

# 

# Client  

# → FastAPI Application  

# → Prometheus  

# → Grafana  

# 

# The API exposes the following endpoints:

# \- /health : service health check

# \- /users : sample business endpoint

# \- /metrics : Prometheus metrics endpoint

# 

# All services run locally using Docker Compose, simulating a real deployment setup.

# 

# ---

# 

# \## Tech Stack

# 

# \- Backend: Python (FastAPI)

# \- Containerization: Docker

# \- Orchestration: Docker Compose

# \- Monitoring: Prometheus, Grafana

# \- CI/CD: GitHub Actions

# \- Testing: pytest

# 

# ---

# 

# \## Project Structure

# 

# devops\_cloud\_ready\_app/

# │

# ├── app/

# │   ├── main.py

# │   └── requirements.txt

# │

# ├── tests/

# │   └── test\_app.py

# │

# ├── monitoring/

# │   └── prometheus.yml

# │

# ├── .github/

# │   └── workflows/

# │       └── ci.yml

# │

# ├── Dockerfile

# ├── docker-compose.yml

# └── README.md

# 

# ---

# 

# \## Running the Project Locally

# 

# \### Prerequisites

# \- Docker Desktop

# \- Docker Compose

# 

# \### Start the full stack

# 

# docker compose up --build

# 

# ---

# 

# \## Available Services

# 

# Service        | URL

# -------------- | --------------------------------

# API Health     | http://localhost:8000/health

# Users API      | http://localhost:8000/users

# Metrics        | http://localhost:8000/metrics

# Prometheus     | http://localhost:9090

# Grafana        | http://localhost:3000

# 

# Grafana default credentials:

# username: admin  

# password: admin  

# 

# ---

# 

# \## Monitoring

# 

# \- Prometheus scrapes metrics from the /metrics endpoint

# \- Metrics collected include:

# &nbsp; - Total number of requests per endpoint

# &nbsp; - Request latency per endpoint

# \- Grafana is used to visualize application health and performance metrics

# 

# This setup provides basic observability similar to what is used in real production environments.

# 

# ---

# 

# \## CI Pipeline (GitHub Actions)

# 

# On every push or pull request, the CI pipeline automatically:

# 1\. Checks out the repository

# 2\. Installs application dependencies

# 3\. Runs automated tests using pytest

# 4\. Builds the Docker image

# 

# This ensures that the application remains stable, testable, and deployable.

# 

# ---

# 

# \## DevOps Concepts Demonstrated

# 

# \- Containerized application development

# \- Reproducible environments

# \- Service orchestration with Docker Compose

# \- Monitoring and observability

# \- Health checks and metrics exposure

# \- Continuous Integration fundamentals

# \- Infrastructure-as-code principles

# 

# ---

# 

# \## What I Learned

# 

# \- How to containerize a backend application using Docker

# \- How to orchestrate multiple services locally with Docker Compose

# \- How monitoring systems like Prometheus collect metrics

# \- How to visualize application metrics using Grafana

# \- How to expose and design health and metrics endpoints

# \- How to automate testing and builds using GitHub Actions

# \- How DevOps tooling fits together in a production-like workflow

# \- How to debug container, network, and port-related issues on Windows using WSL2

# 

# ---

# 

# \## Possible Improvements

# 

# \- Cloud deployment (AWS ECS, GCP, or Azure)

# \- Kubernetes deployment

# \- Persistent storage

# \- Alerting with Prometheus Alertmanager

# \- Secrets management

# \- Environment-specific configurations (dev / prod)

# 

# ---

# 

# \## Purpose

# 

# This project was created to demonstrate practical DevOps skills and to build a strong foundation in modern DevOps tooling and workflows commonly used in production environments.



