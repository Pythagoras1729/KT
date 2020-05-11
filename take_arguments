import argparse
#below argparse for argument to be passed as input for details
PARSER = argparse.ArgumentParser(description='PNS build execution.')
PARSER.add_argument('-START_RPS', type=int, required=True, help='Starting value to perform test')
PARSER.add_argument('-STEP_UP_RATE', type=int, required=True, help='Step value')
PARSER.add_argument('-LOOPS', type=int, required=True, help='No.of loops to perform test')
PARSER.add_argument('-STOP_RPS', type=int, required=True, help='End value to perform test')
PARSER.add_argument('-SERVER', type=str, required=True, help='Server to test')
PARSER.add_argument('-PORT_NUMBER', type=int, required=True, help='Port number')
PARSER.add_argument('-API_PATH', type=str, required=True, help='path to test')
PARSER.add_argument('-API_METHOD', type=str, required=True, help='Method GET|POST|PUT')
ARGS=PARSER.parse_args()
(START_RPS,STEP_UP_RATE,LOOPS,STOP_RPS) = (ARGS.START_RPS,ARGS.STEP_UP_RATE,ARGS.LOOPS,ARGS.STOP_RPS)
(SERVER,PORT_NUMBER,API_PATH,API_METHOD) = (ARGS.SERVER,ARGS.PORT_NUMBER,ARGS.API_PATH,ARGS.API_METHOD)

print('v0:',START_RPS,'vSTEP:',STEP_UP_RATE,'loops:',LOOPS,'v1:',STOP_RPS)
print('server:',SERVER,'port:',PORT_NUMBER,'path:',API_PATH,'method:',API_PATH)


