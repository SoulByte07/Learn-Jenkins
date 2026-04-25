<div align="center">
  <h1 id="readme">Learn Jenkins Mini Project</h1>
  <p>Build, test, and deploy a tiny Flask weather health API with Jenkins, Buildah, and Podman.</p>
  <p>
    <a href="https://github.com/USER/REPO/actions/workflows/WORKFLOW_FILE.yml"><img src="https://img.shields.io/github/actions/workflow/status/USER/REPO/WORKFLOW_FILE.yml?branch=main&style=flat-square" alt="CI/Build"></a>
    <img src="https://img.shields.io/badge/Jenkins-Pipeline-D24939?logo=jenkins&logoColor=white&style=flat-square" alt="Jenkins">
    <img src="https://img.shields.io/badge/platform-Linux-FCC624?logo=linux&logoColor=black&style=flat-square" alt="Linux">
  </p>
</div>

## 🧭 Description
This project is a hands-on playground for learning Jenkins CI/CD with a small Python Flask API. It targets beginners who want to understand image build, test, and deployment stages without enterprise complexity. The key differentiator is a minimal app plus an end-to-end Jenkins pipeline using Buildah and Podman in a local setup.

## ✨ Features
- Exposes a lightweight Flask health endpoint at `/health`.
- Builds a container image through Jenkins with Buildah.
- Runs API tests in the pipeline before deployment.
- Deploys the app container and verifies runtime status with Podman.
- Provides a local Jenkins stack under `Jenkins-Setup/` for reproducible practice.

## 🎬 Demo / Screenshots
![Jenkins Pipeline Demo](docs/demo.gif)

Replace `docs/demo.gif` with your real GIF or screenshot path.

## 🚀 Installation
Prerequisites:
- Python 3.9+
- Docker (for local Jenkins stack)
- Buildah and Podman (for pipeline image build and deploy stages)

1. Clone the repository.
2. Install app dependencies:

```bash
python3 -m pip install -r app/requirements.txt
```

3. Run the API locally:

```bash
python3 app/app.py
```

4. (Optional) Run tests directly:

```bash
python3 -m pytest app/test_app.py -q
```

5. (Optional) Start local Jenkins environment:

```bash
docker compose up --build
```

## 💻 Usage
Query the health endpoint after the service starts on port `5000`:

```bash
curl -s http://localhost:5000/health
# {"service":"weather-api","status":"healthy"}
```

## ⚙️ Configuration
| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `HEALTH_ROUTE` | string | `/health` | API route used for service health checks. |
| `APP_HOST` | string | `0.0.0.0` | Host interface bound by Flask in `app/app.py`. |
| `APP_PORT` | integer | `5000` | Local listening port and container exposed port. |
| `SERVICE_NAME` | string | `weather-api` | `service` value returned by the health response JSON. |
| `IMAGE_TAG` | string | `localhost/weather-api:latest` | Container image tag built and deployed by Jenkins. |
| `BUILDAH_STORAGE_DRIVER` | string | `vfs` | Buildah storage mode used in pipeline. |
| `BUILDAH_ISOLATION` | string | `chroot` | Buildah isolation mode set during image build. |

## ❓ FAQ
### ❓ Why use Buildah and Podman instead of Docker in the pipeline?
This setup avoids Docker socket usage and practices a daemonless container workflow that fits restricted CI environments.

### ❓ Why is the API so small?
The API is intentionally minimal so the focus stays on Jenkins stages, pipeline behavior, and container lifecycle.

### ❓ How do I run Jenkins locally for this project?
Use the compose stack in `Jenkins-Setup/` with `docker compose up --build`, then access Jenkins from the exposed local port configured there.

## 📄 License
Distributed under the [MIT License](LICENSE).
