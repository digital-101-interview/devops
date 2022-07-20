pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
         stage('Clone repository') { 
            steps { 
                script{
                checkout scm
                }
            }
        }
        stage('Test'){
            steps {
                echo "hello world"
            }
        }
        stage('Deploy'){
            steps {
                 sh 'kubectl apply -f k8s/'
            }
        }

    }
}
