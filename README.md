# Project Overview
## What it does:
A lightweight ML model monitoring system that detects data drift, 
model performance degradation, and provides alerting. 
Think of it as a mini-DataDog for ML models.

## Key Features:
- Real-time data drift detection (statistical tests)
- Model performance tracking
- REST API for logging predictions
- Simple dashboard for visualization
- Alerting via webhooks/email

## Tech Stack:
- Backend: FastAPI (Python 3.12)
- Data Processing: Pandas, SciPy (for drift tests)
- Storage: SQLite (start simple, easy to upgrade)
- Testing: Pytest, pytest-cov
- Linting: Ruff, Black, MyPy
- CI/CD: GitHub Actions
- Containerization: Docker