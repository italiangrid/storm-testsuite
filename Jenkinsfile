@Library('sd')_
def kubeLabel = getKubeLabel()

pipeline {

  agent {
    kubernetes {
      label "${kubeLabel}"
      cloud 'Kube mwdevel'
      defaultContainer 'runner'
      inheritFrom 'ci-template'
    }
  }

  options {
    timeout(time: 1, unit: 'HOURS')
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }

  parameters {
    string(defaultValue: "omii006-vm03.cnaf.infn.it", description: '', name: 'STORM_BE_HOST')
    string(defaultValue: "omii003-vm01.cnaf.infn.it:8888", description: '', name: 'CDMI_ENDPOINT')
    string(defaultValue: "to-be-fixed", description: '', name: 'TESTSUITE_EXCLUDE')
    string(defaultValue: "tests", description: '', name: 'TESTSUITE_SUITE')
    string(defaultValue: "/storage", description: '', name: 'STORM_STORAGE_ROOT_DIR')
    string(defaultValue: "italiangrid/storm-testsuite:centos7", description: '', name: 'STORM_TESTSUITE_IMAGE')
  }

  stages {
    stage('run') {
      steps {
        script {
          withCredentials([
            usernamePassword(credentialsId: 'fa43a013-7c86-410f-8a8f-600b92706989', passwordVariable: 'CDMI_CLIENT_SECRET', usernameVariable: 'CDMI_CLIENT_ID'),
            usernamePassword(credentialsId: 'a5ca708a-eca8-4fc0-83cd-eb3695f083a1', passwordVariable: 'IAM_USER_PASSWORD', usernameVariable: 'IAM_USER_NAME')
          ]) {
            def image = "${params.STORM_TESTSUITE_IMAGE}"
            echo "image: ${image}"

            sh "docker pull ${image}"

            def name = "${env.JOB_BASE_NAME}-${env.BUILD_NUMBER}".replaceAll("[^a-zA-Z0-9 ]+","")
            echo "name: ${name}"

            def variables = []
            variables.add("-e TESTSUITE_BRANCH=${env.BRANCH_NAME}")
            variables.add("-e STORM_BE_HOST=${params.STORM_BE_HOST}")
            variables.add("-e CDMI_ENDPOINT=${params.CDMI_ENDPOINT}")
            variables.add("-e TESTSUITE_EXCLUDE=${params.TESTSUITE_EXCLUDE}")
            variables.add("-e TESTSUITE_SUITE=${params.TESTSUITE_SUITE}")
            variables.add("-e CDMI_CLIENT_ID=${CDMI_CLIENT_ID}")
            variables.add("-e CDMI_CLIENT_SECRET=${CDMI_CLIENT_SECRET}")
            variables.add("-e IAM_USER_NAME=${IAM_USER_NAME}")
            variables.add("-e IAM_USER_PASSWORD=${IAM_USER_PASSWORD}")
            variables.add("-e STORM_STORAGE_ROOT_DIR=${params.STORM_STORAGE_ROOT_DIR}")
            envvars = variables.join(' ')
            echo "env-vars: ${envvars}"

            sh returnStatus: true, script: "docker run --name ${name} ${envvars} ${image}"

            sh "docker cp ${name}:/home/tester/storm-testsuite/reports ."
            archive 'reports/**'

            step([$class: 'RobotPublisher',
              disableArchiveOutput: false,
              logFileName: 'log.html',
              otherFiles: '*.png',
              outputFileName: 'output.xml',
              outputPath: "reports",
              passThreshold: 100,
              reportFileName: 'report.html',
              unstableThreshold: 90])
          }
        }
      }
    }
  }

  post {
    failure {
      slackSend color: 'danger', message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Failure (<${env.BUILD_URL}|Open>)"
    }
    changed {
      script {
        if ('SUCCESS'.equals(currentBuild.currentResult)) {
          slackSend color: 'good', message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Back to normal (<${env.BUILD_URL}|Open>)"
        }
      }
    }
  }
}