pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Execute Test Suite') {
            steps {
                bat '''
                    py -m pip install -r requirements.txt
                    py -m pytest test_suite.py --html=report.html --self-contained-html --junitxml=results.xml -v
                '''
            }
        }
    }

    post {
        always {
            // Publish JUnit XML results to Jenkins UI
            junit 'results.xml'
            // Publish HTML report artifact
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Selenium Test Report'
            ])
        }
    }
}