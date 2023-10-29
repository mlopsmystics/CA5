pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -f /src/db/Dockerfile --tag ca4_db .'
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
