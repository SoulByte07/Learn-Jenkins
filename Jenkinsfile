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
                    buildah run weather-test python -m pytest app/test_app.py -q
                    buildah rm weather-test
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    set -e
                    podman rm -f weather-api || true
                    podman run -d --name weather-api -p 5000:5000 localhost/weather-api:latest python app/app.py
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
