pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Docker Compose') {
            steps {
                script {
                    
                    def frontendImageExists = sh(script: 'docker pull mlopsmystics/ca4_web:latest', returnStatus: true) == 0
                    def backendImageExists = sh(script: 'docker pull mlopsmystics/ca4_db:latest', returnStatus: true) == 0

                    if (frontendImageExists && backendImageExists) {
                        sh 'docker-compose up -d'
                    } else {
                        error 'Required Docker images not found on Docker Hub.'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Docker Compose stack started successfully.'
        }
        failure {
            error 'Failed to start Docker Compose stack.'
        }
    }
}