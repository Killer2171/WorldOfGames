MY_AGENT = "YANIV-PC"

node(MY_AGENT){
    stage("clone"){
        git branch: 'main', url: 'https://github.com/Killer2171/WorldOfGames.git'
    }
    stage("show files"){
        //bat "docker build -t worldofgames:yaniv . "
        bat "dir"
    }
}
