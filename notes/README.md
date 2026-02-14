# Notes Service


## Architecture Overview

- Language: Python
- Framework: FastAPI
- Database: MongoDB
- Deployment: Docker + Docker Compose
- Gateway: NGINX (Stage 6)

```
Client
  |
  v
NGINX
  |
  v
Notes Service (FastAPI)
  |
  v
MongoDB
```

---

## Project Structure

```
notes/
├── Dockerfile
├── core/
│   └── config.py
├── db/
│   └── mongo.py
├── main.py
├── models/
│   └── note.py
├── router/
│   └── notes.py
├── services/
│   └── notes_service.py
└── requirements.txt
```

---

## API Endpoints

### Create Note
POST `/notes/`

```bash
curl -X POST http://localhost/notes/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My first note",
    "content": "Hello notes service"
  }'
```

---

### List Notes
GET `/notes/?limit=10&skip=0`

```bash
curl http://localhost/notes/
```

---

### Update Note
PATCH `/notes/{note_id}`

```bash
curl -X PATCH http://localhost/notes/<id> \
  -H "Content-Type: application/json" \
  -d '{"content": "Updated"}'
```

---

### Delete Note
DELETE `/notes/{note_id}`

```bash
curl -X DELETE http://localhost/notes/<id>
```

---

## Health & Readiness

- `/health` – process liveness
- `/ready` – MongoDB readiness (used by Docker healthcheck)

---

---

## Stage 6 Notes

- Runs behind NGINX
- Readiness-based healthcheck
- Independent microservice
