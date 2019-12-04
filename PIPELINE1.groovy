node {      
    stage("Run JOB1-6") {   
        build job: "JOB1-6"
    }

    stage("Run Shell") {
        sh "ls -l"
        sh "pwd"
        sh "env"
    }
}
