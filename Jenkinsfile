pipeline {
    agent any

    stages {
        stage('Run Python Code') {
            steps {
                sh '''
                python3 app.py || python app.py
                '''
            }
        }
    }
}
