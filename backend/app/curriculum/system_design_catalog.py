"""
Module: Comprehensive High-Level and Low-Level System Design Architectures
Covers real-world distributed architectures, capacity planning, database schemas, and trade-offs.
"""

from typing import Dict, List, Any


SYSTEM_DESIGN_CATALOG: List[Dict[str, Any]] = [
    {
        "id": "sys-01",
        "title": "Design a Distributed URL Shortener (TinyURL / Bitly)",
        "difficulty": "Medium",
        "estimated_qps": "10,000 writes/sec, 100,000 reads/sec",
        "storage_estimate": "15 TB over 5 years (Base62 7-char hash)",
        "architecture_summary": """
        1. API Gateway with Rate Limiting (Token Bucket per client IP).
        2. Application Cluster running stateless FastAPI services.
        3. Distributed Unique ID Generator (Snowflake / ZooKeeper range allocator).
        4. Base62 encoding: 62^7 = 3.5 trillion unique short URLs.
        5. Storage Layer: NoSQL Key-Value store (Cassandra / DynamoDB) partitioned by hash key.
        6. Caching Layer: Redis Cluster with LRU eviction caching top 20% URLs (80/20 Pareto rule).
        7. CDN for edge redirection caching.
        """,
        "schema_definition": """
        CREATE TABLE url_mappings (
            short_code VARCHAR(7) PRIMARY KEY,
            original_url TEXT NOT NULL,
            user_id BIGINT,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP,
            click_count BIGINT DEFAULT 0
        );
        CREATE INDEX idx_user_id ON url_mappings(user_id);
        """,
        "key_tradeoffs": [
            "Write throughput vs Read latency (Cache-aside with write-through for hot keys)",
            "Base62 hash collision vs Pre-generated key token range allocator",
            "Cassandra wide-column store for horizontal partition scalability vs PostgreSQL with sharding"
        ]
    },
    {
        "id": "sys-02",
        "title": "Design a High-Throughput Distributed Rate Limiter",
        "difficulty": "Hard",
        "estimated_qps": "500,000 requests/sec across globally distributed edge nodes",
        "storage_estimate": "Redis Cluster in-memory memory footprint ~2GB for 50M active users",
        "architecture_summary": """
        1. Edge API Gateway / Reverse Proxy (Envoy / NGINX) with Redis Lua Scripts.
        2. Sliding Window Log vs Sliding Window Counter Algorithm.
        3. Sliding Window Counter divides the time window into micro-buckets (1 sec chunks).
        4. Atomic Redis pipeline: ZADD, ZREMRANGEBYSCORE, ZCARD, EXPIRE executed in single round-trip.
        5. Fallback local memory cache (Token Bucket) if centralized Redis latency spikes.
        """,
        "schema_definition": """
        -- Redis Key Pattern:
        -- rate:{user_id}:{endpoint_hash}:{window_timestamp} -> Integer Counter
        -- EXPIRE key 60 seconds
        """,
        "key_tradeoffs": [
            "Strict consistency vs Latency budget (Asynchronous batching of request increments)",
            "Sliding Window Log precision vs Memory consumption of individual timestamps"
        ]
    },
    {
        "id": "sys-03",
        "title": "Design a Distributed Message Broker & Streaming Platform (Apache Kafka Style)",
        "difficulty": "Hard",
        "estimated_qps": "2,000,000 messages/sec ingestion",
        "storage_estimate": "100 TB append-only distributed commit logs with 7-day retention",
        "architecture_summary": """
        1. Topics partitioned across multiple Broker nodes for horizontal scalability.
        2. Append-Only Commit Log on disk with OS Page Cache utilization and Zero-Copy DMA (sendfile syscall).
        3. Leader-Follower Partition Replication using In-Sync Replicas (ISR) consensus.
        4. Consumer Groups with distributed partition rebalancing and client-side offset management.
        5. ZooKeeper / KRaft metadata quorum for cluster controller elections.
        """,
        "schema_definition": """
        -- Disk Segment Format:
        -- [Offset: 8B][MessageSize: 4B][CRC32: 4B][Magic: 1B][Attributes: 1B][KeyLength: 4B][Key][PayloadLength: 4B][Payload]
        """,
        "key_tradeoffs": [
            "Disk I/O random writes vs Sequential append with OS page cache zero-copy",
            "At-least-once delivery vs Idempotent producer deduplication with sequence numbers"
        ]
    },
    {
        "id": "sys-04",
        "title": "Design a Video Streaming Architecture with Adaptive Bitrate (Netflix / YouTube)",
        "difficulty": "Hard",
        "estimated_qps": "50,000 concurrent streaming sessions",
        "storage_estimate": "Petabyte scale Object Storage (S3) with multi-resolution transcoding",
        "architecture_summary": """
        1. Ingestion service splitting master video upload into 5-second chunk segments.
        2. Transcoding pipeline generating multi-bitrate streams: 4K, 1080p, 720p, 480p in HLS (m3u8) & MPEG-DASH.
        3. Global Content Delivery Network (CDN) edge servers caching chunk files closest to users.
        4. Adaptive Bitrate Streaming (ABR) client player dynamically adjusting video resolution based on network bandwidth.
        5. User Watch Progress Tracking service persisting heartbeat timestamps to Redis & PostgreSQL.
        """,
        "schema_definition": """
        CREATE TABLE video_assets (
            id UUID PRIMARY KEY,
            course_id INT NOT NULL,
            title VARCHAR(255) NOT NULL,
            master_s3_uri TEXT NOT NULL,
            hls_manifest_url TEXT NOT NULL,
            duration_seconds INT NOT NULL,
            status VARCHAR(50) DEFAULT 'processing',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE user_playback_state (
            user_id BIGINT,
            video_id UUID,
            last_position_seconds INT NOT NULL,
            completed BOOLEAN DEFAULT FALSE,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (user_id, video_id)
        );
        """,
        "key_tradeoffs": [
            "Storage redundancy of multiple bitrate encodings vs User streaming buffering latency",
            "Pre-transcoding all resolutions vs Just-In-Time dynamic chunk transcoding"
        ]
    },
    {
        "id": "sys-05",
        "title": "Design an E-Commerce Payment Gateway & Flash Sale Inventory Lock",
        "difficulty": "Hard",
        "estimated_qps": "20,000 checkout attempts/sec during flash sales",
        "storage_estimate": "Relational ACID database for financial ledger with Redis inventory pre-allocation",
        "architecture_summary": """
        1. Two-Phase Inventory Reservation: Redis Lua script atomically decrements available stock.
        2. Idempotency Key token enforced on checkout submissions to eliminate double-charges.
        3. Payment Gateway Webhook Dispatcher with exponential backoff and dead-letter queues (DLQ).
        4. Double-Entry Accounting Ledger storing debits and credits in immutable append-only transaction logs.
        5. SAGA Distributed Transaction Orchestrator coordinating Order, Payment, and Inventory services.
        """,
        "schema_definition": """
        CREATE TABLE financial_ledger (
            id BIGSERIAL PRIMARY KEY,
            transaction_id UUID NOT NULL,
            account_id BIGINT NOT NULL,
            entry_type VARCHAR(10) NOT NULL CHECK (entry_type IN ('DEBIT', 'CREDIT')),
            amount NUMERIC(12, 2) NOT NULL,
            currency VARCHAR(3) NOT NULL DEFAULT 'USD',
            reference_type VARCHAR(50) NOT NULL,
            reference_id VARCHAR(100) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE INDEX idx_ledger_txn ON financial_ledger(transaction_id);
        CREATE INDEX idx_ledger_account ON financial_ledger(account_id);
        """,
        "key_tradeoffs": [
            "Pessimistic database locking vs Optimistic concurrency control with Redis atomic decrements",
            "Synchronous payment confirmation vs Asynchronous webhook settlement with eventual consistency"
        ]
    }
]
