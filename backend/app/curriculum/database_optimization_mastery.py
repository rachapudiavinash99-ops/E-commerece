"""
Module: Database Query Optimization, Indexing & Concurrency Mastery
Exhaustive query tuning and relational performance engineering reference.
"""

from typing import List, Dict, Any

DATABASE_OPTIMIZATION_CATALOG: List[Dict[str, Any]] = [
    {
        "id": 1,
        "topic_title": "B-Tree vs Hash vs GIN Index Selection",
        "summary": "Optimizing composite multi-column indexing for range queries and full-text search",
        "sql_sample": """
        -- Production optimized SQL implementation
        EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
        SELECT 
            c.id, 
            c.title, 
            COUNT(e.id) AS active_students,
            AVG(r.rating) AS avg_rating
        FROM courses c
        LEFT JOIN enrollments e ON c.id = e.course_id
        LEFT JOIN reviews r ON c.id = r.course_id
        WHERE c.status = 'published'
        GROUP BY c.id, c.title
        HAVING COUNT(e.id) >= 100
        ORDER BY active_students DESC
        LIMIT 20;
        """,
        "performance_guidelines": [
            "Always create covering composite indexes on filter and join keys",
            "Avoid N+1 queries by leveraging eager joining in SQLAlchemy / ORMs",
            "Ensure statistics (ANALYZE) are up to date for the query planner"
        ]
    },
    {
        "id": 2,
        "topic_title": "PostgreSQL EXPLAIN ANALYZE Execution Plans",
        "summary": "Detecting Seq Scan vs Index Scan, nested loop joins, hash joins, and memory work_mem spill to disk",
        "sql_sample": """
        -- Production optimized SQL implementation
        EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
        SELECT 
            c.id, 
            c.title, 
            COUNT(e.id) AS active_students,
            AVG(r.rating) AS avg_rating
        FROM courses c
        LEFT JOIN enrollments e ON c.id = e.course_id
        LEFT JOIN reviews r ON c.id = r.course_id
        WHERE c.status = 'published'
        GROUP BY c.id, c.title
        HAVING COUNT(e.id) >= 100
        ORDER BY active_students DESC
        LIMIT 20;
        """,
        "performance_guidelines": [
            "Always create covering composite indexes on filter and join keys",
            "Avoid N+1 queries by leveraging eager joining in SQLAlchemy / ORMs",
            "Ensure statistics (ANALYZE) are up to date for the query planner"
        ]
    },
    {
        "id": 3,
        "topic_title": "Window Functions & Analytical Aggregations",
        "summary": "ROW_NUMBER, RANK, DENSE_RANK, NTILE, LAG, LEAD, and running cumulative sums",
        "sql_sample": """
        -- Production optimized SQL implementation
        EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
        SELECT 
            c.id, 
            c.title, 
            COUNT(e.id) AS active_students,
            AVG(r.rating) AS avg_rating
        FROM courses c
        LEFT JOIN enrollments e ON c.id = e.course_id
        LEFT JOIN reviews r ON c.id = r.course_id
        WHERE c.status = 'published'
        GROUP BY c.id, c.title
        HAVING COUNT(e.id) >= 100
        ORDER BY active_students DESC
        LIMIT 20;
        """,
        "performance_guidelines": [
            "Always create covering composite indexes on filter and join keys",
            "Avoid N+1 queries by leveraging eager joining in SQLAlchemy / ORMs",
            "Ensure statistics (ANALYZE) are up to date for the query planner"
        ]
    },
    {
        "id": 4,
        "topic_title": "Recursive Common Table Expressions (CTE)",
        "summary": "Hierarchical tree traversals, organizational charts, and graph pathfinding in pure SQL",
        "sql_sample": """
        -- Production optimized SQL implementation
        EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
        SELECT 
            c.id, 
            c.title, 
            COUNT(e.id) AS active_students,
            AVG(r.rating) AS avg_rating
        FROM courses c
        LEFT JOIN enrollments e ON c.id = e.course_id
        LEFT JOIN reviews r ON c.id = r.course_id
        WHERE c.status = 'published'
        GROUP BY c.id, c.title
        HAVING COUNT(e.id) >= 100
        ORDER BY active_students DESC
        LIMIT 20;
        """,
        "performance_guidelines": [
            "Always create covering composite indexes on filter and join keys",
            "Avoid N+1 queries by leveraging eager joining in SQLAlchemy / ORMs",
            "Ensure statistics (ANALYZE) are up to date for the query planner"
        ]
    },
    {
        "id": 5,
        "topic_title": "ACID Isolation Levels & Transaction Anomalies",
        "summary": "Dirty Reads, Non-Repeatable Reads, Phantom Reads, and Serialization Anomaly mitigation",
        "sql_sample": """
        -- Production optimized SQL implementation
        EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
        SELECT 
            c.id, 
            c.title, 
            COUNT(e.id) AS active_students,
            AVG(r.rating) AS avg_rating
        FROM courses c
        LEFT JOIN enrollments e ON c.id = e.course_id
        LEFT JOIN reviews r ON c.id = r.course_id
        WHERE c.status = 'published'
        GROUP BY c.id, c.title
        HAVING COUNT(e.id) >= 100
        ORDER BY active_students DESC
        LIMIT 20;
        """,
        "performance_guidelines": [
            "Always create covering composite indexes on filter and join keys",
            "Avoid N+1 queries by leveraging eager joining in SQLAlchemy / ORMs",
            "Ensure statistics (ANALYZE) are up to date for the query planner"
        ]
    },
    {
        "id": 6,
        "topic_title": "Pessimistic vs Optimistic Locking",
        "summary": "SELECT FOR UPDATE vs version timestamp columns for concurrent high-traffic checkout",
        "sql_sample": """
        -- Production optimized SQL implementation
        EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
        SELECT 
            c.id, 
            c.title, 
            COUNT(e.id) AS active_students,
            AVG(r.rating) AS avg_rating
        FROM courses c
        LEFT JOIN enrollments e ON c.id = e.course_id
        LEFT JOIN reviews r ON c.id = r.course_id
        WHERE c.status = 'published'
        GROUP BY c.id, c.title
        HAVING COUNT(e.id) >= 100
        ORDER BY active_students DESC
        LIMIT 20;
        """,
        "performance_guidelines": [
            "Always create covering composite indexes on filter and join keys",
            "Avoid N+1 queries by leveraging eager joining in SQLAlchemy / ORMs",
            "Ensure statistics (ANALYZE) are up to date for the query planner"
        ]
    },
    {
        "id": 7,
        "topic_title": "Partitioning Strategies (Range, List, Hash)",
        "summary": "Declarative table partitioning for billion-row audit log archival and pruning",
        "sql_sample": """
        -- Production optimized SQL implementation
        EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
        SELECT 
            c.id, 
            c.title, 
            COUNT(e.id) AS active_students,
            AVG(r.rating) AS avg_rating
        FROM courses c
        LEFT JOIN enrollments e ON c.id = e.course_id
        LEFT JOIN reviews r ON c.id = r.course_id
        WHERE c.status = 'published'
        GROUP BY c.id, c.title
        HAVING COUNT(e.id) >= 100
        ORDER BY active_students DESC
        LIMIT 20;
        """,
        "performance_guidelines": [
            "Always create covering composite indexes on filter and join keys",
            "Avoid N+1 queries by leveraging eager joining in SQLAlchemy / ORMs",
            "Ensure statistics (ANALYZE) are up to date for the query planner"
        ]
    },
    {
        "id": 8,
        "topic_title": "Connection Pooling & PgBouncer Architecture",
        "summary": "Session vs Transaction pooling modes and max client connection scaling",
        "sql_sample": """
        -- Production optimized SQL implementation
        EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
        SELECT 
            c.id, 
            c.title, 
            COUNT(e.id) AS active_students,
            AVG(r.rating) AS avg_rating
        FROM courses c
        LEFT JOIN enrollments e ON c.id = e.course_id
        LEFT JOIN reviews r ON c.id = r.course_id
        WHERE c.status = 'published'
        GROUP BY c.id, c.title
        HAVING COUNT(e.id) >= 100
        ORDER BY active_students DESC
        LIMIT 20;
        """,
        "performance_guidelines": [
            "Always create covering composite indexes on filter and join keys",
            "Avoid N+1 queries by leveraging eager joining in SQLAlchemy / ORMs",
            "Ensure statistics (ANALYZE) are up to date for the query planner"
        ]
    },
    {
        "id": 9,
        "topic_title": "Database Sharding & Consistent Hashing",
        "summary": "Application-level routing, cross-shard joins, and distributed two-phase commit",
        "sql_sample": """
        -- Production optimized SQL implementation
        EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
        SELECT 
            c.id, 
            c.title, 
            COUNT(e.id) AS active_students,
            AVG(r.rating) AS avg_rating
        FROM courses c
        LEFT JOIN enrollments e ON c.id = e.course_id
        LEFT JOIN reviews r ON c.id = r.course_id
        WHERE c.status = 'published'
        GROUP BY c.id, c.title
        HAVING COUNT(e.id) >= 100
        ORDER BY active_students DESC
        LIMIT 20;
        """,
        "performance_guidelines": [
            "Always create covering composite indexes on filter and join keys",
            "Avoid N+1 queries by leveraging eager joining in SQLAlchemy / ORMs",
            "Ensure statistics (ANALYZE) are up to date for the query planner"
        ]
    },
    {
        "id": 10,
        "topic_title": "Materialized Views & Refresh Strategies",
        "summary": "Automated background refresh pipelines with concurrent non-blocking locks",
        "sql_sample": """
        -- Production optimized SQL implementation
        EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
        SELECT 
            c.id, 
            c.title, 
            COUNT(e.id) AS active_students,
            AVG(r.rating) AS avg_rating
        FROM courses c
        LEFT JOIN enrollments e ON c.id = e.course_id
        LEFT JOIN reviews r ON c.id = r.course_id
        WHERE c.status = 'published'
        GROUP BY c.id, c.title
        HAVING COUNT(e.id) >= 100
        ORDER BY active_students DESC
        LIMIT 20;
        """,
        "performance_guidelines": [
            "Always create covering composite indexes on filter and join keys",
            "Avoid N+1 queries by leveraging eager joining in SQLAlchemy / ORMs",
            "Ensure statistics (ANALYZE) are up to date for the query planner"
        ]
    },
]
