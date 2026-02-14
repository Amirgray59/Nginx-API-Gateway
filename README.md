# Production-Ready FastAPI Microservices --- Docker + NGINX Gateway + CQRS-lite Architecture

------------------------------------------------------------------------

# Overview

This project demonstrates a **production-oriented backend architecture**
using:

-   FastAPI microservices
-   Docker & docker-compose
-   NGINX as reverse proxy and API gateway
-   CQRS-lite architecture (separated read/write flows)
-   k6 load testing 
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

.
├── ADR-006.md
├── Dockerfile
├── EVIDENCE_ZERO_DOWNTIME.md
├── README.md
├── assets
│   ├── Dockerfile
│   ├── core
│   │   ├── __init__.py
│   │   └── errors.py
│   ├── main.py
│   ├── requirements.txt
│   └── utils
│       ├── __init__.py
│       ├── metadata.py
│       ├── paths.py
│       ├── router.py
│       ├── security.py
│       └── service.py
├── auth
│   ├── Dockerfile
│   ├── README.md
│   ├── api
│   │   └── router.py
│   ├── core
│   │   └── security.py
│   ├── db
│   │   └── postgres.py
│   ├── main.py
│   ├── models
│   │   └── user.py
│   ├── requirements.txt
│   └── services
│       └── auth_service.py
├── docker-compose.yaml
├── k6
│   ├── assets-upload-k6.js
│   ├── notes-k6.js
│   ├── test.jpg
│   └── test.js
├── k6_reports
│   ├── k6-assets-upload-report.md
│   ├── k6-notes-report.md
│   ├── k6-auth-report.md
│   └── k6-report.md
├── nginx
│   └── nginx.conf
├── notes
│   ├── Dockerfile
│   ├── README.md
│   ├── core
│   │   └── config.py
│   ├── db
│   │   └── mongo.py
│   ├── main.py
│   ├── models
│   │   └── note.py
│   ├── requirements.txt
│   ├── router
│   │   └── notes.py
│   └── services
│       └── notes_service.py


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

    k6_reports/
│   ├── k6-assets-upload-report.md
│   ├── k6-notes-report.md
│   ├── k6-auth-report.md
│   └── k6-report.md


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
-   Gateway-based routing
-   Rate limiting
-   GZIP compression
-   Basic caching
-   Health endpoints

------------------------------------------------------------------------

# Deployment Steps

1.  Build containers:

    docker compose build

2.  Start stack:

    docker compose up

3.  Validate health endpoints.

4.  Run k6 performance tests.

5.  Verify SLO thresholds.

------------------------------------------------------------------------

# Acceptance Criteria

-   Services accessible only via NGINX
-   Health checks available
-   Zero downtime deployment demonstrated

------------------------------------------------------------------------
