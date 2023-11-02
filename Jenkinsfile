pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/trickyj/Python_Study_2023.git', branch: 'main')
      }
    }

    stage('Log') {
      steps {
        sh 'ls -la'
      }
    }

    stage('build') {
      steps {
        sh 'docker build -f Python_Study_2023/DockerFile .'
      }
    }

  }
}