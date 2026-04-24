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
                // Input: Dockerfile in the current directory
                sh 'docker build -t weather-api:latest .'
            }
        }

        stage('Run Tests') {
            steps {
                // This starts a container, runs pytest, then destroys it (--rm)
                // Output: Test results (Pass/Fail)
                sh 'docker run --rm weather-api:latest pytest test_app.py'
            }
        }
    }
}
