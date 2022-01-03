

MY_AGENT = "YANIV-PC"

node(MY_AGENT){
    stage("1.GIT"){
        git branch: 'master', url: 'https://github.com/Killer2171/WorldOfGames.git'
    }
    stage("2.DOCKER-BUILD"){
        bat "docker build -t worldofgames:yaniv . "
    }
    stage("2.DOCKER-RUN"){
        def yaniv = bat(script: 'docker run -d -p 8777:5001 worldofgames:yaniv', returnStdout: true).trim()
        println ("Yaniv_result = ${yaniv}")
        println "docker rm  " + yaniv + " -f"


//             bat yaniv = "docker run -d -p 8777:5001 worldofgames:yaniv "
    }
    try{
      stage("3.DOCKER-TEST-SELENIUM"){
      bat "python Test/e2e.py"
    }

        }
    catch(Exception ex) {
      //bat "docker rm" + ret() + "-f"
      println("Catching the exception YANIVVVVVVVVVVVVVVVVV");
      }
}
