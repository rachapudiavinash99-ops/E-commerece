"""
Module: Cloud Native Kubernetes Manifests and Helm Charts Specification
"""

from typing import List, Dict, Any

KUBERNETES_MANIFESTS_CATALOG: List[Dict[str, Any]] = [
    {
        "id": 1,
        "resource_type": "Kubernetes Resource #1",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-1
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v1.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 2,
        "resource_type": "Kubernetes Resource #2",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-2
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v2.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 3,
        "resource_type": "Kubernetes Resource #3",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-3
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v3.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 4,
        "resource_type": "Kubernetes Resource #4",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-4
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v4.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 5,
        "resource_type": "Kubernetes Resource #5",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-5
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v5.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 6,
        "resource_type": "Kubernetes Resource #6",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-6
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v6.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 7,
        "resource_type": "Kubernetes Resource #7",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-7
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v7.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 8,
        "resource_type": "Kubernetes Resource #8",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-8
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v8.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 9,
        "resource_type": "Kubernetes Resource #9",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-9
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v9.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 10,
        "resource_type": "Kubernetes Resource #10",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-10
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v10.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 11,
        "resource_type": "Kubernetes Resource #11",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-11
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v11.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 12,
        "resource_type": "Kubernetes Resource #12",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-12
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v12.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 13,
        "resource_type": "Kubernetes Resource #13",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-13
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v13.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 14,
        "resource_type": "Kubernetes Resource #14",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-14
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v14.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
    {
        "id": 15,
        "resource_type": "Kubernetes Resource #15",
        "manifest_yaml": """
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: codepulse-service-15
          namespace: production
        spec:
          replicas: 3
          template:
            spec:
              containers:
              - name: api
                image: codepulse/api:v15.0
                resources:
                  limits:
                    cpu: "1000m"
                    memory: "1Gi"
        """
    },
]
