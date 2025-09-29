// Jenkinsfile
pipeline {
    agent any

    environment {
        // Use your Docker Hub username
        DOCKER_IMAGE = 'kafkaflow/scientific-calculator-devops-lifecycle'
        DOCKERHUB_CREDENTIALS_ID = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                // Replace with your GitHub repository URL
                git branch: 'main', url: 'https://github.com/lovepop1/scientific-calculator-devops-lifecycle.git'
            }
        }

        stage('Run Tests') {
            agent{
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo 'Running unit tests...'
                sh 'python -m unittest -v test_calculator.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE}"
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Logging in and pushing image..."
                withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
        stage('Deploy with Ansible') {
            steps {
                echo 'Deploying the new container...'
                withCredentials([string(credentialsId: 'vm-sudo-password', variable: 'SUDO_PASS')]) {
                    // Set the password as an environment variable for the ansible-playbook command
                    // This is the standard, secure way to provide a sudo password non-interactively.
                    sh 'ANSIBLE_BECOME_PASS=$SUDO_PASS ansible-playbook -i inventory deploy.yml'
                }
            }
        }
    }
}