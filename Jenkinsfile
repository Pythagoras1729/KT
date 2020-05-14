pipeline{
    agent any
    parameters{
        string(name: 'START_RPS', defaultValue: '', description:'Start value of threads')
        string(name: 'STEP_RPS', defaultValue: '50', description: 'Step up rate')
        string(name: 'LOOPS', defaultValue: '1', description: 'No.of Loops we want to run')
        string(name: 'STOP_RPS', defaultValue: '', description: 'Threshold no.of threads')
        string(name: 'SERVER', defaultValue: '', description: 'Name ofServer we want to test')
        string(name: 'API_PATH', defaultValue: '', description: 'API path')
        string(name: 'PORT_NUMBER', defaultValue: 'N/A', description: 'N/A if not specified')
        string(name: 'API_METHOD', defaultValue:'', description:'(GET, PUT, POST)')
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
                        def cmd= "python  Jenkin/main.py \
                                       -START_RPS ${START_RPS} \
                                       -STEP_UP_RATE ${STEP_RPS}   \
                                       -LOOPS ${LOOPS}         \
                                       -STOP_RPS ${STOP_RPS}   \
                                       -SERVER ${SERVER} \
                                       -API_PATH ${API_PATH}           \
                                       -PORT_NUMBER ${PORT_NUMBER}   \
                                       -API_METHOD ${API_METHOD}"
                        bat """                               
                                ${cmd}
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
