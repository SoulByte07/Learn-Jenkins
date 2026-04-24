# Agent Notes

## Repo shape (high signal only)
- `app/app.py` is the Flask service entrypoint; only route is `GET /health`.
- `app/test_app.py` is the only test file and targets the `/health` endpoint.
- Root `Dockerfile` is for the weather API image.
- Root `Jenkinsfile` is the CI pipeline definition.
- `Jenkins-Setup/` contains the Jenkins runtime image (`Dockerfile`) and local compose stack (`compose.yaml`) used to run Jenkins with Buildah.

## Commands to use (and where)
- Install app deps: `python3 -m pip install -r app/requirements.txt` (run from repo root).
- Run API locally from root: `python3 app/app.py`.
- Run one focused test from root: `python3 -m pytest app/test_app.py -q`.
- Start Jenkins stack from `Jenkins-Setup/`: `docker compose up --build` (or equivalent compose frontend).

## CI / container quirks you should not miss
- Jenkins build stage uses Buildah directly: `buildah bud --storage-driver=vfs -t weather-api:latest .`.
- Jenkins "Run Tests" stage currently only echoes a message; CI does **not** run `pytest` right now.
- `Jenkins-Setup/compose.yaml` sets `privileged: true` and extra `security_opt`; these are intentional for nested container/buildah behavior.

## Important mismatches and constraints
- Python versions differ: `app/.python-version` is `3.14`, but runtime container base image is `python:3.9-slim`; keep runtime compatibility in mind.
- Root `Dockerfile` copies the repo to `/app`, but `CMD ["python", "app.py"]` points to a non-existent path in the current tree (actual file is `app/app.py`). If you touch container startup, verify the command path.
