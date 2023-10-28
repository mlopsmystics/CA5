pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'i200469', url: 'https://github.com/mlopsmystics/CA5.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build-f /src/db/Dockerfile -t ca4_db .'
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerHubCredentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'docker login -u $USERNAME -p $PASSWORD'
                    sh 'docker push ca4_db'
                }
            }
        }
    }
}
