# Production-Ready FastAPI Microservices --- Docker + NGINX Gateway + CQRS-lite Architecture

------------------------------------------------------------------------

# Overview

This project demonstrates a **production-oriented backend architecture**
using:

-   FastAPI microservices
-   Docker & docker-compose
-   NGINX as reverse proxy and API gateway
-   CQRS-lite architecture (separated read/write flows)
-   k6 load testing with SLO validation
-   Zero-downtime deployment preparation

هدف این پروژه شبیه‌سازی یک backend واقعی در سطح production است.

------------------------------------------------------------------------

# Architecture

## Services

-   auth service
-   notes service
-   assets service
-   nginx gateway

## Request Flow

Client → NGINX → Upstream service 

------------------------------------------------------------------------

# Project Structure

├── ADR-006.md
├── Dockerfile
├── README.md
├── assets
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── auth
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── docker-compose.yaml
├── k6
│   └── test.js
├── k6-report.md
├── nginx
│   └── nginx.conf
└── notes
    ├── Dockerfile
    ├── main.py
    └── requirements.txt

------------------------------------------------------------------------

# Docker Setup

## Build and Run

    docker compose up --build

Services run behind NGINX.

Gateway exposed on:

    http://localhost

------------------------------------------------------------------------

# NGINX Responsibilities

-   Reverse proxy routing
-   Load balancing across replicas
-   Rate limiting
-   GZIP compression
-   Request buffering
-   Timeout handling
-   Basic caching (example: notes endpoints)

Example upstream:

    upstream notes_service {
        server notes_v1:8000;
        server notes_v2:8000;
    }

------------------------------------------------------------------------

# Zero Downtime Strategy

Two service versions:

-   v1
-   v2

NGINX upstream distributes traffic.

Deployment flow:

1.  Deploy new container version.
2.  Add to upstream pool.
3.  Remove old version.
4.  No traffic interruption.

------------------------------------------------------------------------

# Health Checks

Each service exposes:

    GET /health

Used for:

-   Monitoring readiness
-   Deployment validation
-   Future orchestration support

------------------------------------------------------------------------

# Performance Testing (k6)

## Why k6

-   Scriptable load tests
-   Threshold-based SLO validation
-   Lightweight and CI-friendly

## Test Scenario

Example:

-   20 virtual users
-   Duration: 30 seconds
-   Requests sent through NGINX gateway

## Example test.js

    import http from 'k6/http';

    export const options = {
      vus: 20,
      duration: '30s',
      thresholds: {
        http_req_duration: ['p(95)<500'],
      },
    };

    export default function () {
      http.get('http://localhost/notes/');
    }

Run:

    k6 run k6/test.js

------------------------------------------------------------------------

# k6 Result Storage

After test execution:

1.  Save summary output.
2.  Export results into:

```{=html}
<!-- -->
```
    k6-report.md

Example contents:

-   p95 latency
-   average latency
-   error rate
-   threshold pass/fail
-   architecture adjustments based on results

Purpose:

-   Performance tracking
-   Architecture decision evidence
-   Documentation for SLO compliance

------------------------------------------------------------------------

# Production Best Practices Implemented

-   Non-root container execution
-   Slim base images
-   Gunicorn + Uvicorn workers
-   Gateway-based routing
-   Rate limiting
-   GZIP compression
-   Basic caching
-   Health endpoints

------------------------------------------------------------------------

# Deployment Steps

1.  Build containers:

```{=html}
<!-- -->
```
    docker compose build

2.  Start stack:

```{=html}
<!-- -->
```
    docker compose up

3.  Validate health endpoints.

4.  Run k6 performance tests.

5.  Verify SLO thresholds.

------------------------------------------------------------------------

# Acceptance Criteria

-   Services accessible only via NGINX
-   Health checks available
-   Load testing completed
-   k6 summary meets SLO targets
-   Zero downtime deployment demonstrated

------------------------------------------------------------------------

# Future Improvements

-   HTTPS/TLS termination
-   Prometheus metrics
-   Distributed tracing
-   Structured logging
-   Kubernetes orchestration

------------------------------------------------------------------------
