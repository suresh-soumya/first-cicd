pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }

    stages {
        stage('Run Python Code') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
