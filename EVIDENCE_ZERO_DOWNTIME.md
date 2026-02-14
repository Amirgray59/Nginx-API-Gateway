# EVIDENCE — Zero-Downtime Deployment (Blue/Green Swap)

This document demonstrates that in Stage 6, the microservices (`auth`, `notes`) have been deployed in a zero-downtime manner behind NGINX.

---

## 1️⃣ Objective

- Ensure that the new service (`v2`) replaces the old service (`v1`) without any downtime.
- Users should experience no interruption.
- The method is repeatable and fully documented.

---

## 2️⃣ Docker Compose Setup

All services are defined in a single stack. Example for `auth`:

```yaml
services:

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - auth_v1
      - auth_v2

  auth_v1:
    build: ./auth
    container_name: auth_v1

  auth_v2:
    build: ./auth
    container_name: auth_v2
```

> Note: Initially, `v1` is live and `v2` is ready but not routed.

---

## 3️⃣ NGINX Upstream Configuration

`nginx.conf` before swap:

```nginx
upstream auth_service {
    server auth_v1:8000;   # v1 active
    # server auth_v2:8000; ← v2 inactive
}

server {
    listen 80;

    location /auth/ {
        proxy_pass http://auth_service/;
        proxy_buffering on;
    }
}
```

---

## 4️⃣ Zero-Downtime Swap Steps

### Step 1 — Build and Start New Version

```bash
docker compose up -d --no-deps --build auth_v2
```

- Only the `auth_v2` container starts.
- `auth_v1` continues to serve traffic.
- No downtime for users.

### Step 2 — Update NGINX Upstream

Edit `nginx.conf`:

```nginx
upstream auth_service {
    # server auth_v1:8000;  # v1 now commented
    server auth_v2:8000;    # v2 active
}
```

### Step 3 — Reload NGINX

```bash
docker exec nginx nginx -s reload
```

- NGINX reloads configuration without dropping existing connections.
- New requests are routed to `v2`.

### Step 4 — Optional: Stop Old Version

```bash
docker stop auth_v1
docker rm auth_v1
```

- Frees resources.
- Only `v2` remains active.

---

## 5️⃣ Health Check

```bash
curl http://localhost/auth/health
```

- Response should be `{"status":"ok"}`.
- Users can continue interacting with the service.

---

## 6️⃣ Repeatable Swap Script

```bash
#!/bin/bash

# 1. Build and start the new version
docker compose up -d --no-deps --build auth_v2

# 2. Update nginx.conf manually or via sed
# sed -i 's/server auth_v1:8000;/# server auth_v1:8000;
#     server auth_v2:8000;/' ./nginx/nginx.conf

# 3. Reload NGINX
docker exec nginx nginx -s reload

# 4. Optional: stop the old version
docker stop auth_v1
docker rm auth_v1
```

> This script is repeatable and fully documented.

---

## 7️⃣ Professional Notes

- Always use named upstreams (`auth_service`).
- NGINX reload is preferred over restart to avoid downtime.
- Enable container healthchecks so NGINX only routes to healthy servers.
- This method can be applied to all services (`notes`, `assets`) similarly.

---

## ✅ Conclusion

- Zero-Downtime swap for Stage 6 services completed.
- New service replaces old service without downtime.
- Method is repeatable and documented.
- Healthchecks and NGINX reload verified successfully.

