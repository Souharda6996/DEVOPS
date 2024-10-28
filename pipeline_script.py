pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[credentialsId: 'cf4c3581-e55a-4c7c-b4ea-1427910ac133', url: 'https://github.com/Souharda6996/DEVOPS.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: 'cf4c3581-e55a-4c7c-b4ea-1427910ac133', url: 'https://github.com/Souharda6996/DEVOPS.git'
                bat 'python sort.py'
                
            }
        }
        stage('Test') {
            steps {
                echo "Testing is done"
            }
        }
    }
}
