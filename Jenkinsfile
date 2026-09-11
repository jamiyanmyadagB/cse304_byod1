pipeline {
    agent any

    environment {
        IMAGE_NAME = "koorkon/myapp"
        IMAGE_TAG  = "v1.${BUILD_NUMBER}"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jamiyanmyadagB/cse304_byod1.git', credentialsId: 'github-creds'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f myapp-container || true'
                sh 'docker run -d --name myapp-container -p 3000:3000 $IMAGE_NAME:$IMAGE_TAG'
            }
        }
    }
}
