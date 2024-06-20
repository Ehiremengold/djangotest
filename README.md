# Django AWS Docker Sentry CI/CD Repository

Welcome to my repository where I've been learning and experimenting with Django, AWS, Docker, Sentry, and setting up CI/CD pipelines using GitHub Actions.

## Overview

This project is aimed at exploring various technologies and practices related to modern web development and deployment. Below is an overview of what's included in this repository:

- **Django**: Python-based web framework used for building the web application.
- **AWS**: Integration and deployment to Amazon Web Services for cloud services.
- **Docker**: Containerization of the Django application for consistency and scalability.
- **Sentry**: Integration for error tracking and monitoring in production.
- **CI/CD with GitHub Actions**: Setting up automated build, test, and deployment workflows using GitHub Actions.

## Getting Started

To get started with this project, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ehiremengold/django-aws-docker-sentry-cicd.git
   cd django-aws-docker-sentry-cicd
2. **Set up the environment**:
    Ensure you have Docker installed locally.
    Create a .env file and configure necessary environment variables (e.g., AWS credentials, Sentry DSN).
3. Run the application locally
   `docker-compose up`
4. Explore and modify:
    Explore the source directory to view and modify the Django project.
    Modify Docker configurations (Dockerfile, docker-compose.yml) as needed for your deployment.
## Deployment
    This project is set up for deployment to AWS using Docker containers. GitHub Actions workflows (`.github/workflows/`) are configured to automate CI/CD processes. Ensure you have configured secrets and necessary environment variables in your GitHub repository settings for deployment.
