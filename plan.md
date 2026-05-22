
# Project PRD

## Internal AI Ticket & Workflow Platform

A backend-heavy system that teaches:

* APIs
* auth
* DBs
* async
* queues
* caching
* debugging
* system flow
* AI integration
* deployment

without unnecessary complexity.

---

# Core Concept

A company has:

* support tickets,
* AI processing jobs,
* logs,
* users,
* background tasks.

Your system manages everything.

---

# Tech Constraints

## Backend

* Python
* FastAPI

## Database

* PostgreSQL

## Cache / Queue

* Redis

## Async Workers

* Celery / RQ / Dramatiq

## Deployment

* Docker

No frontend initially.

Postman/swagger only.

---

# Features

---

# Phase 1 — Core Backend

## Auth

Users can:

* signup
* login
* refresh token
* logout

Roles:

* admin
* engineer
* customer

---

## Ticket System

Tickets have:

* title
* description
* status
* priority
* assigned user
* timestamps

Operations:

* create
* update
* assign
* close
* list/filter

---

## Comments

Users can:

* add comments
* edit comments
* fetch comments

---

# Phase 2 — Async Systems

## AI Processing Job

When ticket is created:

* background job starts
* simulated AI analysis runs
* generates:

  * severity
  * suggested fix
  * tags

This MUST happen asynchronously.

---

## Job Queue

Implement:

* pending
* processing
* failed
* retry

---

# Phase 3 — Caching + Performance

## Redis

Cache:

* ticket list
* user session
* analytics endpoint

Implement:

* cache invalidation

---

# Phase 4 — System Awareness

## Logging

Store:

* API errors
* failed jobs
* retry logs

---

## Metrics Endpoint

Return:

* open tickets
* failed jobs
* avg processing time

---

# Phase 5 — Deployment

Dockerize:

* API
* DB
* Redis
* worker

Use docker-compose.

---

# Non-Functional Requirements

You MUST:

* structure code cleanly
* separate layers
* handle errors properly
* validate requests
* use environment variables
* write modular code

---

# Critical Rule

DO NOT optimize for:

* fancy architecture
* perfect design
* resume value

Optimize for:

# understanding.

---
