pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/trickyj/Python_Study_2023.git', branch: 'main')
      }
    }

    stage('Log') {
      parallel {
        stage('Log') {
          steps {
            sh 'ls -la'
          }
        }

        stage('Front-End unit test') {
          steps {
            sh 'cd Python_basics && npm i && npm run test:unit'
          }
        }

      }
    }

  }
}