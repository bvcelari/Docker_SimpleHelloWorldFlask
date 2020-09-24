node {
    checkout([
        $class: 'GitSCM', 
        branches: [[name: 'ff5062eab9e50d9b614f79366467d2a7ea2ace6c']], 
        doGenerateSubmoduleConfigurations: false, 
        extensions: [], 
        submoduleCfg: [], 
        userRemoteConfigs: [[url: 'https://github.com/bvcelari/maven-helloworld']]])
    sh 'ls -al'
}
