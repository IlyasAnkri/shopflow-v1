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
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pytest test_api.py --junitxml=reports/result.xml
                '''
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