MY_AGENT = "YANIV-PC"

node(MY_AGENT){
    stage("1.GIT"){
        git branch: 'master', url: 'https://github.com/Killer2171/WorldOfGames.git'
    }
    stage("2.DOCKER-BUILD"){
        bat "docker build -t worldofgames:yaniv . "
    }
    stage("2.DOCKER-RUN"){
         script {
            container_id = bat(script: "docker run -d -p 8777:5001 worldofgames:yaniv", returnStdout: true).trim()
         }
    }
    try{
      stage("3.DOCKER-TEST-SELENIUM"){
      bat "python Test/e2e.py"
    }

        }
    catch(Exception ex) {
      println(${container_id});
      }
}
