# Auth Service (FastAPI + PostgreSQL)

This service provides authentication endpoints for a microservice stack.
It is designed to run independently but be deployed together with other
services (notes, assets, etc.) behind NGINX in Stage 6.

------------------------------------------------------------------------

## Features

-   User registration
-   User login
-   JWT token generation
-   Password hashing (pbkdf2_sha256)
-   PostgreSQL database via SQLAlchemy
-   Environment-based configuration (.env)
-   Docker-ready

------------------------------------------------------------------------

## Tech Stack

-   FastAPI
-   SQLAlchemy
-   PostgreSQL
-   Passlib (pbkdf2_sha256)
-   python-jose (JWT)
-   Docker

------------------------------------------------------------------------

## Environment Variables (.env)

Example:

``` env
DATABASE_URL=postgresql://postgres:example@postgres:5432/auth_db
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

------------------------------------------------------------------------

## Run with Docker Compose

``` bash
docker compose up --build
```

Check logs:

``` bash
docker compose logs -f auth
```

------------------------------------------------------------------------

## API Endpoints

Base URL (behind nginx example):

    http://localhost/auth

Local direct access example:

    http://localhost:8001

------------------------------------------------------------------------

# 1️⃣ Health Check

## Request

``` bash
curl http://localhost/auth/health
```

## Response

``` json
{
  "status": "ok"
}
```

------------------------------------------------------------------------

# 2️⃣ Register User

## Request

``` bash
curl -X POST http://localhost/auth/register \
  -H "Content-Type: application/json" \
  -d '{
        "email": "test@example.com",
        "password": "strongpassword123"
      }'
```

## Example Response

``` json
{
  "id": 1,
  "email": "test@example.com"
}
```

------------------------------------------------------------------------

# 3️⃣ Login

## Request

``` bash
curl -X POST http://localhost/auth/login \
  -H "Content-Type: application/json" \
  -d '{
        "email": "test@example.com",
        "password": "strongpassword123"
      }'
```

## Example Response

``` json
{
  "access_token": "JWT_TOKEN_HERE",
  "token_type": "bearer"
}
```

Save the token:

``` bash
TOKEN="JWT_TOKEN_HERE"
```

------------------------------------------------------------------------

## Project Structure (Example)

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


------------------------------------------------------------------------

## Password Hashing

This service uses:

    pbkdf2_sha256

Advantages:

-   No 72-byte password limit (unlike bcrypt)
-   Secure and modern
-   Compatible with Passlib

------------------------------------------------------------------------

## Development Tips

Rebuild after code changes:

``` bash
docker compose down
docker compose up --build 
```

------------------------------------------------------------------------

## Stage 6 Integration

-   Service runs independently
-   Exposed only via NGINX reverse proxy
-   Healthchecks enabled
-   No direct internal coupling required

------------------------------------------------------------------------
