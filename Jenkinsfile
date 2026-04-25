pipeline {
    agent any
    stages {
        stage('Initialize') {
            steps {
                sh "echo 'Building for Soul using Buildah (No Sockets!)'"
            }
        }
        stage('Build Image') {
            steps {
                // 'bud' is short for Build-Using-Dockerfile
                sh 'buildah bud --isolation=chroot --storage-driver=vfs -t localhost/weather-api:latest -t weather-api:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    set -e
                    buildah rm weather-test || true
                    buildah from --name weather-test localhost/weather-api:latest
                    buildah run weather-test python -m pip install --no-cache-dir pytest==8.3.5
                    buildah run weather-test python -m pytest app/test_app.py -q
                    buildah rm weather-test
                '''
            }
        }
        stage('Dependency Scan') {
            steps {
                sh '''
                    set -e
                    buildah rm weather-audit || true
                    buildah from --name weather-audit localhost/weather-api:latest
                    buildah run weather-audit python -m pip install --no-cache-dir pip-audit==2.8.0 bandit==1.7.9
                    buildah run weather-audit pip-audit --strict
                    buildah run weather-audit bandit -q -r app -ll
                    buildah rm weather-audit
                '''
            }
        }
        stage('Image Scan') {
            steps {
                sh '''
                    set -e
                    TRIVY_VERSION=0.65.0
                    TMP_DIR=$(mktemp -d)
                    trap 'rm -rf "$TMP_DIR"' EXIT
                    curl -sSfL -o "$TMP_DIR"/trivy.tar.gz "https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_Linux-64bit.tar.gz"
                    curl -sSfL -o "$TMP_DIR"/trivy_checksums.txt "https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_checksums.txt"
                    grep " trivy_${TRIVY_VERSION}_Linux-64bit.tar.gz$" "$TMP_DIR"/trivy_checksums.txt | sha256sum -c -
                    tar -xzf "$TMP_DIR"/trivy.tar.gz -C "$TMP_DIR" trivy
                    "$TMP_DIR"/trivy image --severity HIGH,CRITICAL --exit-code 1 localhost/weather-api:latest
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    set -e
                    podman rm -f weather-api || true
                    podman run -d --name weather-api -p 127.0.0.1:5000:5000 localhost/weather-api:latest
                    sleep 3
                    podman ps --filter name=weather-api --filter status=running --format '{{.Names}}' | grep -q '^weather-api$'
                '''
            }
        }
    }
    post {
        always {
            sh 'buildah rmi --prune || true'
            sh 'podman image prune -f || true'
            echo 'Cleaned up build artifacts. Staying minimal.'
        }
    }
}
