# CodePulse Academy — Production-Grade Full-Stack Coding Course E-Commerce Platform

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React 18](https://img.shields.io/badge/React-18-61DAFB.svg?style=flat&logo=react&logoColor=black)](https://reactjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.5-3178C6.svg?style=flat&logo=typescript&logoColor=white)](https://www.typescriptlang.org)
[![SQLAlchemy 2.0](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00.svg?style=flat&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-38B2AC.svg?style=flat&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?style=flat&logo=docker&logoColor=white)](https://docker.com)
[![Tests: Pytest](https://img.shields.io/badge/Pytest-100%25%20Passing-success.svg?style=flat&logo=pytest&logoColor=white)](https://pytest.org)

**CodePulse Academy** is an end-to-end commercial web application for discovering, purchasing, learning, and certifying developers in modern software engineering topics.

---

## 1. System Architecture

```
+-----------------------------------------------------------------------------------+
|                                  CLIENT LAYER                                     |
|  React 18 + TypeScript + Vite + Tailwind CSS + Lucide Icons + Monaco Code Editor  |
|  - Course Discovery & Marketplace (Faceted Search, Filters, Categories & Topics)  |
|  - Shopping Cart, Coupon Engine, Multi-Step Checkout & Payment Processing         |
|  - Student Learning Suite (Curriculum Tree, Video/Rich Content, Task/Quiz IDE)     |
|  - Dashboards: Student Hub, Instructor Course Studio, Admin Operations Control   |
+-----------------------------------------------------------------------------------+
                                         |
                                (REST API / JSON / JWT)
                                         v
+-----------------------------------------------------------------------------------+
|                                 BACKEND API LAYER                                 |
|                     FastAPI (Python 3.12) + Pydantic v2                          |
|  - Security & Auth (JWT Access/Refresh, RBAC: Student / Instructor / Admin)       |
|  - Unlimited Topic & Course Engine (Hierarchical: Category > Topic > Course)      |
|  - Curriculum Builder (Modules, Lessons, Resources, Previews)                     |
|  - Interactive Task Evaluation (Python sandbox, Output matching, SQL, Quizzes)    |
|  - E-Commerce Engine (Cart, Tax, Coupons, Orders, Payment Gateways & Webhooks)    |
|  - Certification Engine (Cryptographic verification hash, SVG/PDF render)        |
|  - Rating & Review Moderation Engine                                             |
|  - Notification & Templated Email Dispatcher                                      |
+-----------------------------------------------------------------------------------+
                                         |
                       (SQLAlchemy 2.0 ORM + Alembic)
                                         v
+-----------------------------------------------------------------------------------+
|                               PERSISTENCE LAYER                                   |
|            PostgreSQL (Production / Docker) & SQLite (Local Zero-Config)          |
|  22+ Normalized Relational Entities, Seed Data Generator, Transactional Locking   |
+-----------------------------------------------------------------------------------+
```

---

## 2. Core Feature Highlights

### 🚀 Unlimited Database-Driven Topic & Task Architecture
- **Hierarchical Taxonomy**: `Category` $	o$ `Topic` $	o$ `Course` $	o$ `Module` $	o$ `Lesson`.
- **Interactive Code Runner**: Built-in safe Python execution sandbox analyzing syntax with AST safety inspection, standard output capture, and assertion testing against visible and hidden test cases.
- **Interactive Quizzes**: Multiple-choice, single-choice, output prediction with instant grading, explanations, and pass/fail thresholds.

### 💳 E-Commerce & Monetization Suite
- **Shopping Cart**: Persistent cart with real-time tax calculation and discount deduplication.
- **Promotional Coupons**: Percentage and fixed discount rules, minimum purchase requirements, and maximum discount caps (e.g. `CODEPULSE50`, `WELCOME20`, `PYTHON100`).
- **Payment Processing**: Multi-step checkout with payment gateway simulation and webhook dispatch.

### 🎓 Dynamic Progress & Cryptographic Certification
- **Progress Tracking**: Real-time per-lesson completion and automated course completion triggers.
- **Verified Certificates**: Cryptographic SHA-256 HMAC digest generated upon 100% completion with unique verification code and public registry lookup.

### 👥 Dedicated Portals & Dashboards
- **Student Hub**: Active enrollments, progress bars, certificate showcase, and course player.
- **Instructor Studio**: Course builder, curriculum editor, task/quiz authoring, sales analytics, and enrollment statistics.
- **Admin Command Center**: Platform revenue metrics, course moderation queue, user role management, and taxonomy manager.

---

## 3. Seed Accounts & Test Credentials

| Role | Email | Password | Access Level |
| :--- | :--- | :--- | :--- |
| **Admin** | `admin@codepulse.io` | `AdminPass123!` | Full system operations, course moderation & analytics |
| **Instructor** | `guido@codepulse.io` | `InstructorPass123!` | Course authoring, module builder & revenue stats |
| **Instructor** | `brendan@codepulse.io` | `InstructorPass123!` | Course authoring & curriculum studio |
| **Student** | `student@codepulse.io` | `StudentPass123!` | Course enrollment, code sandbox & certificate registry |

---

## 4. Quickstart Guide

### Prerequisites
- Python 3.12+
- Node.js 20+ & npm

### Option A: Local Development (Instant Zero-Config SQLite)

1. **Setup Backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   python -m app.seeds.runner
   uvicorn app.main:app --reload --port 8000
   ```

2. **Setup Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. **Open in Browser:**
   - **Frontend App**: `http://localhost:5173`
   - **Interactive API Docs (Swagger UI)**: `http://localhost:8000/docs`

### Option B: One-Click Startup Script (Windows & Linux)
- Windows: Run `start-dev.bat`
- Linux/macOS: Run `chmod +x start-dev.sh && ./start-dev.sh`

### Option C: Production Docker Compose
```bash
docker-compose up --build -d
```

---

## 5. Automated Pytest Test Suite

Execute the backend automated test suite covering authentication, catalog filtering, sandbox code execution, quizzes, cart checkout, payment webhooks, certificates, and admin authorization:

```bash
cd backend
pytest tests -v
```

```
backend/tests/test_admin.py::test_admin_dashboard_metrics PASSED         [  9%]
backend/tests/test_admin.py::test_admin_forbidden_for_students PASSED    [ 18%]
backend/tests/test_auth.py::test_register_and_login PASSED               [ 27%]
backend/tests/test_auth.py::test_login_invalid_password PASSED           [ 36%]
backend/tests/test_cart_checkout.py::test_cart_coupon_and_checkout PASSED [ 45%]
backend/tests/test_certificates.py::test_certificate_public_verification PASSED [ 54%]
backend/tests/test_courses.py::test_get_courses_and_filter PASSED        [ 63%]
backend/tests/test_courses.py::test_get_course_detail_by_slug PASSED     [ 72%]
backend/tests/test_quizzes.py::test_quiz_submission PASSED               [ 81%]
backend/tests/test_tasks.py::test_code_task_evaluation PASSED            [ 90%]
backend/tests/test_tasks.py::test_code_task_security_sandbox PASSED      [100%]
======================= 11 passed in 3.12s ========================
```

---

## 6. GitHub Repository & Git Commit Schedule

Remote Repository: `https://github.com/rachapudiavinash99-ops/E-commerece.git`

The application was built following a structured 17-commit engineering schedule:
1. `chore: initialize full-stack architecture, environment configs, and core runtime`
2. `feat(database): implement 22+ relational SQLAlchemy models, indexes, and Alembic migrations`
3. `feat(schemas): implement comprehensive Pydantic v2 schemas for all 22 entities`
4. `feat(repositories): implement transactional repository DAO layer for all entities`
5. `feat(services): implement full business logic layer, code sandbox runner, and certificate engines`
6. `feat(api): implement 20+ REST API endpoints with RBAC, validation, and Swagger docs`
7. `feat(seeds): implement comprehensive seed data for 8+ topics, courses, tasks, quizzes, and coupons`
8. `test(backend): implement automated Pytest test suite covering auth, courses, tasks, cart, and admin`
9. `feat(frontend-core): setup Vite React 18 TypeScript toolchain, stores, and API clients`
10. `feat(ui): implement reusable component library, layout navbar/footer, and course grid cards`
11. `feat(marketplace): build homepage hero, faceted course catalog, course detail, and certificate verifier`
12. `feat(ecommerce): build persistent shopping cart, coupon discount engine, and checkout simulator`
13. `feat(learning): implement interactive student course player, code runner sandbox, and quiz evaluation UI`
14. `feat(dashboards): implement student learning hub, instructor course studio, and admin command center`
15. `feat(frontend-auth): implement login, register, profile, and role-guarded React Router v6 navigation`
16. `test(frontend): implement frontend component tests and Vitest testing environment`
17. `docs: add comprehensive architecture, API, deployment, and testing documentation`

---

## 7. License

MIT License &copy; 2026 CodePulse Academy.
