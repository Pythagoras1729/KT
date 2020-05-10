pipeline{
    agent any
    parameters{
        string(name: 'START_RPS', defaultValue: '', description:'Start rate in rps(requests per second)')
        string(name: 'STEP_RPS', defaultValue: '50', description: 'Step rps')
        string(name: 'LOOPS', defaultValue: '1', description: 'NO.of Loops we want to run')
        string(name: 'STOP_RPS', defaultValue: '', description: 'Stop rps')
        string(name: 'CLUSTER_NAME', defaultValue: '', description: 'Name of cluster under test')
        string(name: 'PATH', defaultValue: '', description: 'API path')
        string(name: 'PORT_NUMBER', defaultValue: 'N/A', description: 'Port number where we want to perform test')
        string(name: 'METHOD', defaultValue:'', description:'Method (GET, PUT, POST)')
    }
    stage('run test'){
        println("Test starts")
        try{
            def cmd= "python  \
                           -START_RPS ${START_RPS} \
                           -STEP_UP_RATE ${STEP_RPS}   \
                           -LOOPS ${LOOPS}         \
                           -STOP_RPS ${STOP_RPS}   \
                           -SERVER ${CLUSTER_NAME} \
                           -API_PATH ${PATH}           \
                           -PORT_NUMBER ${PORT_NUMBER}   \
                           -API_METHOD ${METHOD}"

            sh """  
                  echo "exporting PythonPath ... "
                  echo path: ${PATH}
                  
                  echo \$PYTHONPATH
                  ${cmd}
               """
        }catch (err) {
            println("Some Error while running the PNS_RATE_FINDER job")
        }
    }
}