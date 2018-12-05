pipeline {
    
    agent any
   
    stages {
      stage('setup pipenv') {
        steps {
           sh 'python -m pip install pipenv'
           sh 'PIPENV_MAX_SUBPROCESS=3 python -m pipenv install -v --dev'
        }
      }
      stage('test') {
        steps {
           sh 'python -m pipenv run test '
        }
      }
      stage('assets') {
        steps {
           sh 'python -m pipenv run assets '
        }
      }
      stage('deploy') {
        steps {
            sh 'ls -al'
            dir('ansible'){
              sh 'ls -al'
              ansiblePlaybook installation: 'system python3 ansible', forks: 2, disableHostKeyChecking: true, credentialsId: 'b82afff2-15e7-4f0f-a66c-a1ff5cf0e338', inventory: 'hosts', vaultCredentialsId: '971b21bf-0aa6-4b2f-8344-45ddc623530a', playbook: 'playbook.yml'
            }
        }
        when {
          branch 'master'
       }
     }
   }
} 

