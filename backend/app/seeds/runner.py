import json
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, create_tables
from app.core.security import get_password_hash, generate_certificate_code
from app.models import (
    User, Category, Topic, Course, Module, Lesson, LessonResource,
    CodingTask, TestCase, Quiz, QuizQuestion, QuizOption, Coupon,
    Review, Enrollment, Certificate
)
from app.utils.certificate_generator import generate_certificate_svg
from app.utils.crypto import generate_certificate_hash


def seed_database():
    create_tables()
    db: Session = SessionLocal()

    if db.query(User).filter(User.email == "admin@codepulse.io").first():
        print("Database already contains seed records. Skipping...")
        db.close()
        return

    print("Seeding database with realistic coding courses, topics, tasks, and quizzes...")

    # 1. Users
    admin = User(
        email="admin@codepulse.io",
        password_hash=get_password_hash("AdminPass123!"),
        full_name="Alex Vance (Admin)",
        role="admin",
        headline="Chief Architect & Platform Director",
        bio="Lead systems architect overseeing curriculum standards and platform operations.",
        avatar_url="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150",
        is_active=True,
        is_verified=True
    )
    db.add(admin)

    instructor1 = User(
        email="guido@codepulse.io",
        password_hash=get_password_hash("InstructorPass123!"),
        full_name="Guido Rossum",
        role="instructor",
        headline="Principal Python Architect & Author",
        bio="Veteran engineer with 20+ years building large scale distributed Python systems.",
        avatar_url="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150",
        is_active=True,
        is_verified=True
    )
    instructor2 = User(
        email="brendan@codepulse.io",
        password_hash=get_password_hash("InstructorPass123!"),
        full_name="Brendan Eich",
        role="instructor",
        headline="Full-Stack JavaScript & TypeScript Pioneer",
        bio="Specialist in modern browser runtimes, React architecture, and TypeScript tooling.",
        avatar_url="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150",
        is_active=True,
        is_verified=True
    )
    instructor3 = User(
        email="ada@codepulse.io",
        password_hash=get_password_hash("InstructorPass123!"),
        full_name="Dr. Ada Lovelace",
        role="instructor",
        headline="Algorithms & Systems Design Specialist",
        bio="Former research scientist focused on algorithmic efficiency and data structures.",
        avatar_url="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=150",
        is_active=True,
        is_verified=True
    )
    db.add_all([instructor1, instructor2, instructor3])

    student = User(
        email="student@codepulse.io",
        password_hash=get_password_hash("StudentPass123!"),
        full_name="Devin Miller",
        role="student",
        headline="Aspiring Full-Stack Software Engineer",
        bio="Passionate developer eager to master Python, TypeScript, and modern distributed architecture.",
        avatar_url="https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=150",
        is_active=True,
        is_verified=True
    )
    db.add(student)
    db.commit()

    # 2. Categories
    cat_swe = Category(name="Software Engineering", slug="software-engineering", icon="code", description="Core fundamentals of software engineering, OOP, and system design.", display_order=1)
    cat_web = Category(name="Web Development", slug="web-development", icon="globe", description="Modern frontend and backend frameworks: React, FastAPI, Node, Next.js.", display_order=2)
    cat_ai = Category(name="Data Science & AI", slug="data-science-ai", icon="brain", description="Machine learning, neural networks, data analysis, and AI application engineering.", display_order=3)
    cat_devops = Category(name="DevOps & Cloud", slug="devops-cloud", icon="cloud", description="Containerization, CI/CD pipelines, Kubernetes, Docker, and AWS.", display_order=4)
    cat_db = Category(name="Databases & SQL", slug="databases-sql", icon="database", description="Relational and NoSQL databases, query optimization, and schema architecture.", display_order=5)

    db.add_all([cat_swe, cat_web, cat_ai, cat_devops, cat_db])
    db.commit()

    # 3. Topics
    t_python = Topic(category_id=cat_swe.id, name="Python", slug="python", icon="file-code", is_popular=True, description="Modern Python 3.12 syntax, concurrency, typing, and OOP.")
    t_fastapi = Topic(category_id=cat_web.id, name="FastAPI", slug="fastapi", icon="zap", is_popular=True, description="Asynchronous RESTful APIs with Pydantic and OpenAPI.")
    t_react = Topic(category_id=cat_web.id, name="React & TypeScript", slug="react-typescript", icon="layout", is_popular=True, description="Component-driven UI, state management, and strict TypeScript.")
    t_dsa = Topic(category_id=cat_swe.id, name="Data Structures & Algorithms", slug="data-structures-algorithms", icon="git-branch", is_popular=True, description="Graph traversal, dynamic programming, and complexity analysis.")
    t_docker = Topic(category_id=cat_devops.id, name="Docker & Containers", slug="docker-containers", icon="box", is_popular=True, description="Containerization, multi-stage builds, and Docker Compose.")
    t_sql = Topic(category_id=cat_db.id, name="PostgreSQL & SQL", slug="postgresql-sql", icon="database", is_popular=True, description="Relational queries, indexing strategies, and ACID transactions.")
    t_rust = Topic(category_id=cat_swe.id, name="Rust", slug="rust", icon="shield", is_popular=False, description="Memory safety without garbage collection, borrowing, and concurrency.")
    t_sysdesign = Topic(category_id=cat_swe.id, name="System Design", slug="system-design", icon="cpu", is_popular=True, description="High-scale distributed systems, caching, message queues, and replication.")

    db.add_all([t_python, t_fastapi, t_react, t_dsa, t_docker, t_sql, t_rust, t_sysdesign])
    db.commit()

    # 4. Courses
    c1 = Course(
        instructor_id=instructor1.id,
        topic_id=t_python.id,
        title="Python 3.12 Masterclass: From Fundamentals to Architecture",
        slug="python-312-masterclass-fundamentals-to-architecture",
        subtitle="Master modern Pythonic idioms, type hinting, decorators, generators, asyncio, and clean code.",
        description="Master modern Python 3.12 syntax, OOP, concurrency, generators, and clean architecture.",
        short_description="Master modern Python 3.12 syntax, OOP, concurrency, generators, and clean architecture.",
        price=89.99,
        discount_price=49.99,
        level="all_levels",
        duration_hours=24.5,
        thumbnail_url="https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=600",
        promo_video_url="https://www.youtube.com/embed/kqtD5dpn9C8",
        requirements="Basic computer literacy. No prior coding experience required.",
        what_you_will_learn="Write idiomatic Python 3.12, Master OOP & Metaclasses, Asyncio concurrency, Interactive test-driven problem solving.",
        target_audience="Beginners wanting a solid foundation and developers transitioning to Python.",
        status="published",
        is_featured=True,
        is_bestseller=True,
        average_rating=4.9,
        review_count=18,
        student_count=142,
        published_at=datetime.now(timezone.utc)
    )

    c2 = Course(
        instructor_id=instructor1.id,
        topic_id=t_fastapi.id,
        title="Production FastAPI & SQLAlchemy 2.0 Microservices",
        slug="production-fastapi-sqlalchemy-microservices",
        subtitle="Build robust, asynchronous REST APIs with Pydantic v2, JWT Auth, Docker, and Alembic.",
        description="Architect scalable asynchronous APIs using FastAPI, Pydantic v2, PostgreSQL, and Docker.",
        short_description="Architect scalable asynchronous APIs using FastAPI, Pydantic v2, PostgreSQL, and Docker.",
        price=99.99,
        discount_price=59.99,
        level="intermediate",
        duration_hours=18.0,
        thumbnail_url="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600",
        promo_video_url="https://www.youtube.com/embed/kqtD5dpn9C8",
        requirements="Intermediate Python knowledge.",
        what_you_will_learn="Asynchronous routing, Pydantic v2 validation, SQLAlchemy 2.0 ORM, JWT security & RBAC.",
        target_audience="Python developers wanting to build backend APIs.",
        status="published",
        is_featured=True,
        is_bestseller=False,
        average_rating=4.8,
        review_count=12,
        student_count=98,
        published_at=datetime.now(timezone.utc)
    )

    c3 = Course(
        instructor_id=instructor2.id,
        topic_id=t_react.id,
        title="Modern React 18 & TypeScript: Full-Stack UI Engineering",
        slug="modern-react-18-typescript-fullstack-ui",
        subtitle="Build scalable web applications with React Hooks, Zustand state management, and Tailwind CSS.",
        description="Complete React 18 roadmap with TypeScript, Vite, Zustand, Tailwind CSS, and custom hooks.",
        short_description="Complete React 18 roadmap with TypeScript, Vite, Zustand, Tailwind CSS, and custom hooks.",
        price=79.99,
        discount_price=39.99,
        level="intermediate",
        duration_hours=20.0,
        thumbnail_url="https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=600",
        promo_video_url="https://www.youtube.com/embed/kqtD5dpn9C8",
        requirements="Basic JavaScript (ES6) knowledge.",
        what_you_will_learn="Component architecture, custom hooks, Zustand stores, Tailwind UI design.",
        target_audience="Frontend engineers and full-stack developers.",
        status="published",
        is_featured=True,
        is_bestseller=True,
        average_rating=4.9,
        review_count=24,
        student_count=210,
        published_at=datetime.now(timezone.utc)
    )

    c4 = Course(
        instructor_id=instructor3.id,
        topic_id=t_dsa.id,
        title="Data Structures & Algorithms: The Technical Interview Playbook",
        slug="data-structures-algorithms-interview-playbook",
        subtitle="Ace Big Tech coding interviews with pattern-based problem solving in Python and TypeScript.",
        description="Pattern-oriented coding interview preparation with interactive problem solving.",
        short_description="Pattern-oriented coding interview preparation with interactive problem solving.",
        price=119.99,
        discount_price=69.99,
        level="advanced",
        duration_hours=32.0,
        thumbnail_url="https://images.unsplash.com/photo-1516116211227-bbc13c7343e6?w=600",
        promo_video_url="https://www.youtube.com/embed/kqtD5dpn9C8",
        requirements="Programming proficiency in at least one language.",
        what_you_will_learn="Big-O complexity, Graph traversals (BFS/DFS), Dynamic Programming, Binary Search.",
        target_audience="Engineers preparing for technical coding interviews.",
        status="published",
        is_featured=False,
        is_bestseller=True,
        average_rating=5.0,
        review_count=31,
        student_count=340,
        published_at=datetime.now(timezone.utc)
    )

    db.add_all([c1, c2, c3, c4])
    db.commit()

    # 5. Modules & Lessons for Course 1
    m1 = Module(course_id=c1.id, title="Module 1: Python Fundamentals & Data Types", order_index=1)
    m2 = Module(course_id=c1.id, title="Module 2: Functions, Scopes & Decorators", order_index=2)
    m3 = Module(course_id=c1.id, title="Module 3: Object-Oriented Programming (OOP)", order_index=3)
    db.add_all([m1, m2, m3])
    db.commit()

    l1_1 = Lesson(
        module_id=m1.id,
        title="1. Introduction to Modern Python 3.12",
        slug="intro-modern-python-312",
        lesson_type="video",
        content="Welcome to Python 3.12! In this lesson, we explore the Python runtime environment, virtual environments, and key language semantics.",
        video_url="https://www.youtube.com/embed/kqtD5dpn9C8",
        duration_minutes=15,
        order_index=1,
        is_preview=True
    )
    l1_2 = Lesson(
        module_id=m1.id,
        title="2. Interactive Task: Variable Manipulation & Calculations",
        slug="task-variable-manipulation",
        lesson_type="coding_task",
        content="Coding Task: Calculate Total Course Price with Discount. Implement calculate_discount() in the interactive editor.",
        duration_minutes=20,
        order_index=2,
        is_preview=False
    )
    l1_3 = Lesson(
        module_id=m1.id,
        title="3. Knowledge Check: Python Data Types Quiz",
        slug="quiz-python-data-types",
        lesson_type="quiz",
        content="Test your understanding of immutability, lists, tuples, and dictionary lookups.",
        duration_minutes=10,
        order_index=3,
        is_preview=False
    )
    db.add_all([l1_1, l1_2, l1_3])
    db.commit()

    # 6. Coding Task
    task1 = CodingTask(
        lesson_id=l1_2.id,
        title="Calculate Final Discount Price",
        instructions="Implement the function calculate_discount(original_price: float, discount_percent: float) -> float.",
        task_type="coding",
        difficulty="easy",
        language="python",
        starter_code="""def calculate_discount(original_price: float, discount_percent: float) -> float:
    # Your code here
    pass
""",
        solution_code="""def calculate_discount(original_price: float, discount_percent: float) -> float:
    discount_amount = original_price * (discount_percent / 100.0)
    return round(original_price - discount_amount, 2)
""",
        hints="Remember: final = original - (original * (percent / 100)). Use round(val, 2).",
        points=10,
        time_limit_seconds=5
    )
    db.add(task1)
    db.commit()

    tc1 = TestCase(task_id=task1.id, input_data="calculate_discount(100.0, 20.0)", expected_output="80.0", is_hidden=False, explanation="100 - 20% = 80.0")
    tc2 = TestCase(task_id=task1.id, input_data="calculate_discount(49.99, 10.0)", expected_output="44.99", is_hidden=False, explanation="49.99 - 10% = 44.991 -> 44.99")
    tc3 = TestCase(task_id=task1.id, input_data="calculate_discount(200.0, 50.0)", expected_output="100.0", is_hidden=True, explanation="Hidden edge case test")
    db.add_all([tc1, tc2, tc3])
    db.commit()

    # 7. Quiz & Questions
    quiz1 = Quiz(
        lesson_id=l1_3.id,
        title="Python Data Types & Memory Model Quiz",
        description="Verify your understanding of Python primitive vs reference types.",
        pass_percentage=70,
        time_limit_minutes=10,
        max_attempts=3
    )
    db.add(quiz1)
    db.commit()

    q1 = QuizQuestion(
        quiz_id=quiz1.id,
        question_text="Which of the following built-in types in Python is IMMUTABLE?",
        question_type="single_choice",
        explanation="Tuples, strings, integers, and floats are immutable in Python.",
        points=5,
        order_index=1
    )
    db.add(q1)
    db.commit()

    db.add_all([
        QuizOption(question_id=q1.id, option_text="List", is_correct=False, order_index=1),
        QuizOption(question_id=q1.id, option_text="Dictionary", is_correct=False, order_index=2),
        QuizOption(question_id=q1.id, option_text="Tuple", is_correct=True, order_index=3),
        QuizOption(question_id=q1.id, option_text="Set", is_correct=False, order_index=4)
    ])

    q2 = QuizQuestion(
        quiz_id=quiz1.id,
        question_text="What is the output of bool([]) in Python?",
        question_type="single_choice",
        explanation="An empty list evaluates to False in a boolean context.",
        points=5,
        order_index=2
    )
    db.add(q2)
    db.commit()

    db.add_all([
        QuizOption(question_id=q2.id, option_text="True", is_correct=False, order_index=1),
        QuizOption(question_id=q2.id, option_text="False", is_correct=True, order_index=2),
        QuizOption(question_id=q2.id, option_text="TypeError", is_correct=False, order_index=3)
    ])
    db.commit()

    # 8. Coupons
    cp1 = Coupon(
        code="CODEPULSE50",
        description="Special Launch 50% Discount on all orders",
        discount_type="percentage",
        discount_value=50.0,
        minimum_amount=20.0,
        maximum_discount=100.0,
        usage_limit=500,
        active=True
    )
    cp2 = Coupon(
        code="WELCOME20",
        description="New Student $20 Fixed Discount",
        discount_type="fixed_amount",
        discount_value=20.0,
        minimum_amount=40.0,
        usage_limit=1000,
        active=True
    )
    cp3 = Coupon(
        code="PYTHON100",
        description="100% Free Scholarship Coupon for Python Masterclass",
        discount_type="percentage",
        discount_value=100.0,
        minimum_amount=0.0,
        usage_limit=50,
        active=True
    )
    db.add_all([cp1, cp2, cp3])
    db.commit()

    # 9. Realistic Reviews
    r1 = Review(
        user_id=student.id,
        course_id=c1.id,
        rating=5,
        title="Outstanding depth and hands-on tasks!",
        comment="The interactive code runner built right into the lessons makes all the difference. Highly recommended for any serious developer!",
        is_verified_purchase=True,
        status="approved",
        helpful_count=7
    )
    r2 = Review(
        user_id=student.id,
        course_id=c3.id,
        rating=5,
        title="Clean architecture and modern TypeScript patterns",
        comment="Best React 18 course I have taken. The explanation of custom hooks and state machines was crystal clear.",
        is_verified_purchase=True,
        status="approved",
        helpful_count=4
    )
    db.add_all([r1, r2])
    db.commit()

    # 10. Sample Student Enrollment & Certificate
    enr = Enrollment(
        user_id=student.id,
        course_id=c1.id,
        completion_percentage=100.0,
        is_completed=True,
        completed_at=datetime.now(timezone.utc)
    )
    db.add(enr)
    db.commit()

    cert_code = "CERT-CP-2026-DEMO99"
    issue_date_str = datetime.now(timezone.utc).strftime("%B %d, %Y")
    cert_hash = generate_certificate_hash(student.full_name, c1.title, cert_code, issue_date_str)
    svg_data = generate_certificate_svg(student.full_name, c1.title, instructor1.full_name, cert_code, issue_date_str, 100.0)

    cert = Certificate(
        user_id=student.id,
        course_id=c1.id,
        certificate_number=cert_code,
        verification_code=cert_code,
        verification_hash=cert_hash,
        final_grade=100.0,
        issued_at=datetime.now(timezone.utc),
        svg_content=svg_data
    )
    db.add(cert)
    db.commit()

    print("Seed data successfully injected into database!")
    db.close()


if __name__ == "__main__":
    seed_database()
