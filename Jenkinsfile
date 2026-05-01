pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-notepad .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop my-container || true
                docker rm my-container || true
                docker run -d -p 5000:5000 --name my-container my-notepad
                '''
            }
        }
    }
}
