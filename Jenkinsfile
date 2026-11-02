pipeline {
    agent any // Le pipeline s'exécutera sur l'agent disponible (notre Jenkins local)

    stages {
        stage('Checkout') {
            steps {
                // Jenkins récupère automatiquement le code depuis Git
                checkout scm
            }
        }

        stage('Install & Test') {
            steps {
                sh '''
                rm -rf venv test.db
                python3 -m venv venv
                ./venv/bin/pip install -r requirements.txt
                export DATABASE_URL="sqlite:///./test.db"
                ./venv/bin/pytest test_api.py --junitxml=reports/result.xml --cov=. --cov-report=xml:reports/coverage.xml
                rm -f test.db
                '''
            }
        }

	stage('SonarQube Analysis') {
            environment {
                scannerHome = tool 'sonar-scanner'
            }
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh '''
                    ${scannerHome}/bin/sonar-scanner \
                    -Dsonar.projectKey=shopflow-backend \
                    -Dsonar.sources=. \
                    -Dsonar.python.coverage.reportPaths=reports/coverage.xml
                    '''
                }
            }
        }
	stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t shopflow-backend .'
            }
        }
        
        stage('Push') {
            steps {
                // On commentera cette partie tant qu'on n'a pas configuré les identifiants Docker Hub dans Jenkins
                echo "L'image sera poussée sur Docker Hub plus tard."
            }
        }
    }
}
