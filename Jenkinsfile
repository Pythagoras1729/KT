pipeline{
    agent any
    parameters{
        string(name: 'START_RPS', defaultValue: '', description:'Start rate in rps(requests per second)')
        string(name: 'STEP_RPS', defaultValue: '50', description: 'Step rps')
        string(name: 'LOOPS', defaultValue: '1', description: 'NO.of Loops we want to run')
        string(name: 'STOP_RPS', defaultValue: '', description: 'Stop rps')
        string(name: 'CLUSTER_NAME', defaultValue: '', description: 'Name of cluster under test')
        string(name: 'API_PATH', defaultValue: '', description: 'API path')
        string(name: 'PORT_NUMBER', defaultValue: 'N/A', description: 'Port number where we want to perform test')
        string(name: 'METHOD', defaultValue:'', description:'Method (GET, PUT, POST)')
    }
    stages{
        stage('Set Environment'){
            steps{
                script{
                    env.PATH="C:\\WINDOWS\\SYSTEM32;"+env.PATH
                }
            }
        }
        stage('run test'){
            steps{
                script{
                    println("Test starts")
                    try{
                        def cm= "python  Jenkins_take_arguments.py \
                                       -START_RPS ${START_RPS} \
                                       -STEP_UP_RATE ${STEP_RPS}   \
                                       -LOOPS ${LOOPS}         \
                                       -STOP_RPS ${STOP_RPS}   \
                                       -SERVER ${CLUSTER_NAME} \
                                       -API_PATH ${API_PATH}           \
                                       -PORT_NUMBER 80   \
                                       -API_METHOD ${METHOD}"
                        bat """
                              ${cm}
                           """
                    }
                    catch (err) {
                        println("Some Error while running the task:\n err:"+err)
                    } //end of catch
                }//end of script
            }//end of steps
        }//end of stage
    }//end of stages
}//end of pipeine
