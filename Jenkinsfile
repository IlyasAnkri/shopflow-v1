pipeline {
    agent any // Le pipeline s'exécutera sur l'agent disponible (notre Jenkins local)

    stages {
        stage('Checkout') {
            steps {
                // Jenkins récupère automatiquement le code depuis Git
                checkout scm
            }
        }

        stage('Install') {
            steps {
                // Installe les dépendances Python
                sh 'pip install -r backend/requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Lance les tests avec Pytest
                sh 'pytest backend/tests/ --junitxml=reports/result.xml'
            }
        }

        stage('Build image') {
            steps {
                // Construit l'image Docker (grâce à notre configuration DooD)
                sh 'docker build -t shopflow-backend ./backend'
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