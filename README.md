# Reservation System

This project is a comprehensive reservation system incorporating best practices for database management, caching, queue management, and distributed locking using Flask, SQLAlchemy, Redis, AWS SQS, and Docker.

## Directory Structure

reservation_system/
│
├── app/
│   ├── init.py
│   ├── models.py
│   ├── views.py
│   ├── tasks.py
│   ├── cache.py
│   ├── lock.py
│   ├── performance.py
│   └── utils.py
├── tests/
│   ├── test_models.py
│   ├── test_views.py
│   └── test_tasks.py
├── migrations/
│   └── …
├── run_analysis.py
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore

## Setup

### 1. Clone the Repository

```sh
git clone <repository-url>
cd reservation_system
```
### 2. Create and Activate a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
## Running the Application
### 1. Initialize the Database
```sh
python -c "from app import create_app; app = create_app(); with app.app_context(): from app.models import db; db.create_all()"
```
### 2. Start the Flask Application
```sh
python app.py
```
The application will be available at http://127.0.0.1:5000.
## Redis Setup for Caching and Distributed Locking
### Ensure Redis is running on your machine. You can use Docker to run Redis:
```sh
docker run -d -p 6379:6379 redis
```
## AWS SQS for Queue Management
### Ensure you have set up AWS credentials on your machine. Install boto3 if not already installed:
```sh
pip install boto3
```
## Performance Testing
### Load Testing
```sh
from app.performance import load_test
load_test(your_function, times)
```
### Stress Testing
```sh
from app.performance import stress_test
stress_test(your_function, times, concurrent_users)
```
## Running Tests
### To run the tests, use the following command:
```sh
python -m unittest discover tests
```
## Docker Setup
### 1. Build Docker Image
```sh
docker build -t reservation-system .
```
### 2. Run Docker Compose
```sh
docker-compose up --build -d
```
## Continuous Integration with GitHub Actions
### A sample GitHub Actions workflow file is provided in .github/workflows/ci.yml.
