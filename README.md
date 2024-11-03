# Email Validator Application

The Email Validator is a simple web API that checks the validity of email addresses. It is built with Flask and deployed on Kubernetes using Minikube.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [License](#license)

## Features

- **Email Validation**: Validates email addresses for proper format.
- **RESTful API**: Provides an easy-to-use endpoint for integration.
- **Scalable Deployment**: Deployed on Kubernetes for scalability and reliability.

## Prerequisites

- **Docker** installed on your machine.
- **Minikube** installed and running.
- **Kubectl** command-line tool installed.

## Installation

### 1. Clone the Repository

```bash
git clone https://your-repository-url.git
cd your-repository-directory
```

### 2. Start Minikube

Start Minikube if it's not already running:

```bash
minikube start
```

### 3. Build Docker Images

Build the Docker images for the application:

```bash
# Switch to Minikube's Docker daemon
eval $(minikube docker-env)

# Build the proper solution image
docker build -t email-validator-proper:latest ./proper_solution

# Build the fallback solution image
docker build -t email-validator-fallback:latest ./fallback_solution
```

### 4. Deploy to Kubernetes

Apply the Kubernetes manifests to deploy the application:

```bash
kubectl apply -f k8s/
```

## Usage

### Accessing the Application

Since direct access may not be available due to network configurations, use port forwarding to access the application:

```bash
kubectl port-forward service/email-validator-service 8080:80
```

Keep this terminal window open to maintain the port forwarding session.

### Sending a Validation Request

In a new terminal window, you can test the application using `curl`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"email": "test@example.com"}' \
http://localhost:8080/validate
```

**Expected Response:**

```json
{"valid": true}
```

Replace `"test@example.com"` with the email address you want to validate.

## API Reference

### POST `/validate`

Validates the provided email address.

- **URL**: `/validate`
- **Method**: `POST`
- **Headers**: `Content-Type: application/json`
- **Body Parameters**:
  - `email` (string): The email address to validate.
- **Success Response**:
  - **Code**: `200 OK`
  - **Content**:

    ```json
    {"valid": true}
    ```

- **Error Response**:
  - **Code**: `400 Bad Request`
  - **Content**:

    ```json
    {"error": "Invalid request"}
    ```

## License

This project is licensed under the MIT License.

