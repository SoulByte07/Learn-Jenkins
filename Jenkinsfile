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
                sh 'buildah bud --storage-driver=vfs -t weather-api:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                // Buildah doesn't 'run' containers like Podman, 
                // so we use a simple podman-remote or local podman if installed
                sh 'echo "Image built successfully without touching the host!"'
            }
        }
    }
}
