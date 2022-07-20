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
                 curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
                 chmod +x ./kubectl
                 mv ./kubectl /usr/local/bin
            }
        }
        stage('Deploy'){
            steps {
                 sh 'kubectl apply -f k8s/'
            }
        }

    }
}
