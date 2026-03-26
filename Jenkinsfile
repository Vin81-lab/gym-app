pipeline {
    agent any

    environment {
        DOCKER_PATH = "/opt/homebrew/bin"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                PYTHONPATH=. pytest
                '''
            }
        }

        stage('Build Docker') {
            steps {
                sh '''
                export PATH=/usr/local/bin:%PATH
                docker build -t gym-app .
                '''
            }
        }
    }
}
