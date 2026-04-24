pipeline {
    agent any 

    stages {
        stage('Initialize') {
            steps {
                // Jenkins automatically clones the code from Git before this
                sh 'echo "Building project: ${env.JOB_NAME} on Arch Linux"'
            }
        }

        stage('Build Image') {
            steps {
                // Input: podmanfile in the current directory
                sh 'podman build -t weather-api:latest .'
            }
        }

        stage('Run Tests') {
            steps {
                // This starts a container, runs pytest, then destroys it (--rm)
                // Output: Test results (Pass/Fail)
                sh 'podman run --rm weather-api:latest pytest test_app.py'
            }
        }
    }
}
