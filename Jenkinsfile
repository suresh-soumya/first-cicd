pipeline {
    agent any

    stages {
        stage('Run Python Code') {
            steps {
                sh '''
                apt update
                apt install -y python3
                python3 app.py
                '''
            }
        }
    }
}
