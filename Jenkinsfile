pipeline{
  agent any
  environment{
    PYTHON_PATH='C:\\Program Files\\Python311;C:\\Program Files\\Python311\\Scripts'
    PATH = "C:\\WINDOWS\\SYSTEM32"
    SONAR_SCANNER_PATH='C:\\Users\\nnavi\\OneDrive\\Desktop\\sonar-scanner-cli-6.2.1.4610-windows-x64\\sonar-scanner-6.2.1.4610-windows-x64\\bin'
  }
  stages{
    stage('Checkout'){
      steps{
        checkout scm
      }
    }
    stage('SonarAnalysis'){
      environment{
        SONAR_TOKEN=credentials('sonarqube-token')
      }
      steps{
        bat '''
        set PATH=%PYTHON_PATH%;%SONAR_SCANNER_PATH%;%PATH%
        sonar-scanner -Dsonar.projectKey=sonardt5 ^
                      -Dsonar.sources=. ^
                      -Dsonar.host.url=http://localhost:9000 ^
                      -Dsonar.token=%SONAR_TOKEN%
        '''
      }
    }
  }
  post{
    success{
      echo "went good"
    }
    failure{
      echo "went bad"
    }
  }
}
