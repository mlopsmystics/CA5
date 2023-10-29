pipeline {
    agent any
    environment {
        BACKEND_IMAGE = 'mlopsmystics/backend:latest'
        MYSQL_ROOT_PASSWORD = 'root'
        MYSQL_DATABASE = 'TODO'
    }

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build and push MySQL Docker image
                    docker.build("my-mysql-image:${env.BUILD_NUMBER}")
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerHubCredentials') {
                        docker.image("my-mysql-image:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }
    }
        
}