pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Test') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
                sh 'python manage.py test'
            }
        }
        
        stage('Docker Build') {
            steps {
                sh 'ansible-playbook docker_build.yml'
            }
        }
        
        stage('Docker Push') {
            steps {
                sh 'ansible-playbook docker_push.yml'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'ansible-playbook deploy.yml'
            }
        }
    }
}
