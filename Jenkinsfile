pipeline{
    agent any
    parameters{
        string(name: 'START_RPS', defaultValue: '', description:'Start value of threads')
        string(name: 'STEP_RPS', defaultValue: '', description: 'Step up rate')
        string(name: 'LOOPS', defaultValue: '', description: 'No.of Loops we want to run')
        string(name: 'STOP_RPS', defaultValue: '', description: 'Threshold no.of threads')
        string(name: 'E2E_50_THRESHOLD', defaultValue: '0', description: 'e2e .50 threshold ms')
        string(name: 'E2E_90_THRESHOLD', defaultValue: '0', description: 'e2e .90 threshold ms')
        string(name: 'E2E_99_THRESHOLD', defaultValue: '0', description: 'e2e .99 threshold ms')
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
                        def cmd= "python  Jenkin/main.py \
                                       -START_RPS ${START_RPS} \
                                       -STEP_UP_RATE ${STEP_RPS}   \
                                       -LOOPS ${LOOPS}         \
                                       -STOP_RPS ${STOP_RPS}   \
                                       -E2E_50_THRESHOLD ${E2E_50_THRESHOLD} \
                                       -E2E_90_THRESHOLD ${E2E_90_THRESHOLD} \
                                       -E2E_99_THRESHOLD ${E2E_99_THRESHOLD} \
                                       -SERVER ${SERVER} \
                                       -API_PATH ${API_PATH}           \
                                       -PORT_NUMBER ${PORT_NUMBER}   \
                                       -API_METHOD ${API_METHOD}"
                        bat """                               
                                ${cmd}
                           """
                }//end of script
            }//end of steps
        }//end of stage
    }//end of stages
    post{
        always{
                archiveArtifacts'./Jenkins/Data/CSV/Aggregate_Result.csv'
        }//end of always
    }//end of post
}//end of pipeine
