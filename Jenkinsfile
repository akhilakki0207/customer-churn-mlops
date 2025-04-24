pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t churn-api .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    sh 'echo "$PASS" | docker login -u "$USER" --password-stdin'
                    sh 'docker push churn-api'
                }
            }
        }
    }
}
