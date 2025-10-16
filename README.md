🏠 Real Estate Backend API

A fully featured real estate backend API built with Python and Django, designed for scalability, maintainability, and production readiness.
It includes authentication, asynchronous processing, containerized deployment, and a clean modular structure to support real-world real estate operations.
---

🚀 System Features
🧩 Core Architecture

Custom User Model ➔ extends Django’s default for flexibility in user management.

JWT Authentication ➔ secure token-based authentication for API clients.

UUID Primary Keys ➔ ensures data consistency and avoids predictable IDs.

Django Signals ➔ event-driven logic for decoupled and maintainable code.

Django Filtering ➔ robust search and filtering across listings, users, and transactions.

---
<br>
⚙️ DevOps & Infrastructure

Dockerized Setup ➔ all services (web, db, celery, redis, nginx) run in isolated containers.

PostgreSQL Database ➔ reliable and performant relational storage inside Docker.

Nginx ➔ acts as a web server and reverse proxy, serving static and media files efficiently.

Shell Scripts ➔ custom scripts to automate setup, migrations, and test execution.

---
<br>
⚡ Asynchronous Processing

Celery + Redis ➔ handle background jobs, notifications, and long-running tasks asynchronously.

Flower Dashboard ➔ real-time monitoring of Celery workers and task queues.

---
<br>

🧪 Quality & Testing

Pytest ➔ modern testing framework for clean and maintainable test cases.

Coverage Reports ➔ ensures high-quality, well-tested codebase.

Continuous Integration Ready ➔ easily extendable for CI/CD pipelines.

---

⚠️ **Status:** The API is currently **under development**. 
