# 📚 Book Catalog Microservices Project (DevOps Edition)

This project demonstrates a Python-based **microservices architecture** managed with **DevOps best practices**. It includes services built with Django, Flask, and FastAPI, containerized using Docker, orchestrated with Docker Compose, and continuously integrated via GitHub Actions.

---

## 🧩 Architecture

```
book-catalog/
├── user_service/          # User Auth via Django
├── book_service/           # Book CRUD via Flask
├── recommendation_service/ # Recommendations via FastAPI
├── docker-compose.yml            # Docker orchestration
└── .github/workflows/devops.yml  # CI Workflow
```

---

## 🚀 Services Overview

### 1. **Django User Service**
- Handles user registration and authentication.

### 2. **Flask Book Service**
- Provides endpoints for managing books.

### 3. **FastAPI Recommendation Service**
- Suggests books based on popularity or preference.

---

## 🐳 Docker Setup

### ✅ Build and Run All Services

```bash
docker-compose up --build
```

### Access Services Locally

| Service     | URL                        |
|-------------|----------------------------|
| Django      | http://localhost:8000      |
| Flask       | http://localhost:5000/books |
| FastAPI     | http://localhost:8001/recommend |

---

## ✅ GitHub Actions (CI)

Located at: `.github/workflows/devops.yml`

Runs on every push and pull request to:
- Build Docker containers
- Run Python tests for each service
- Lint Python code (optional)

---

## 🧪 Local Testing

### Using Docker Compose:
```bash
docker-compose build
docker-compose up
```

### Manual Test Execution:
```bash
# Django
cd user_service
python manage.py test

# Flask
cd book_service
pytest

# FastAPI
cd recommendation_service
pytest
```

---

## 📦 Future Enhancements

- Add database support (PostgreSQL/MongoDB)
- Deploy to cloud (Render, EC2, Railway)
- Add Prometheus + Grafana for monitoring
- Migrate to Kubernetes (Helm, GKE/EKS)
- Secure with HTTPS (Certbot + NGINX)

---
## 🧑‍💻 Author

Noel Emmanuel Full Stack Developer & DevOps Enthusiast
GitHub: [@De-pitcher](https://github.com/De-pitcher)
LinkedIn: [noel-emma](https://linkedin.com/in/noel-emma)

## 📄 License

MIT License. Use for educational and professional learning purposes.