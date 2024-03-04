# Fishsearcher Application Deployment Guide

## Prerequisites

- Docker installed and running
- Minikube installed and running
- kubectl installed and configured
- Helm installed

## Setup Instructions

### 1. Start Minikube

Start your Minikube environment with the following command:

```bash
minikube start
```

### 2. Set Docker Environment

Configure your shell to use Minikube's Docker daemon:

```bash
eval $(minikube docker-env)
```

### 3. Build Docker Image

Navigate to your application directory and build the Docker image:

```bash
docker build -t fishsearcher:latest .
docker tag fishsearcher:latest peretzrickett/fishsearcher:latest
docker login
docker push peretzrickett/fishsearcher:latest
```

### 4. Deploy with Helm

First, initialize a Helm chart in your project if not already done. Then, deploy your application using Helm:

```bash
helm install fishsearcher-release ./fishsearcher-chart
```

Or, if upgrading

```bash
helm upgrade fishsearcher-release ./fishsearcher-chart
```

### 5. Access the Application

To access the Fishsearcher application, use the following command to get the URL:

```bash
minikube service fishsearcher-release-fishsearcher-chart --url
```

## Updating the Application

If you make changes to your application and need to update the deployment, follow these steps:

1. Rebuild your Docker image with the new changes.
2. Update the Helm deployment to use the new image version. If the image tag remains the same (`latest`), you may need to force the Kubernetes deployment to pull the new image:

    ```bash
    kubectl rollout restart deployment fishsearcher-deployment
    ```

   Alternatively, if using a new image tag, update your Helm chart values to reflect the new tag and run:

    ```bash
    helm upgrade fishsearcher peretzrickett/fishsearcher
    ```

### Note

Ensure your Helm chart values.yaml file correctly references the Docker image and tag used by your deployment.