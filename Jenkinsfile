pipeline{
    agent any
    stages{
        stage('Environment Setup'){
            steps{
                sh "podman build -t weather-app:latest ."
            }
        }
        stage('Test'){
            steps{
                sh "podman run --rm weather-app:latest pytest test_app.py"}
            }
        }
        stage('Deploy'){
            steps{
                // stop the old container if it exists and start a new one
                sh "podman stop weather-container || true"
                sh "podman rm weather-container || true"
                sh "podman run -d --name weather-container -p 5000:5000 weather-app:latest"
            }
        }
    }
}
