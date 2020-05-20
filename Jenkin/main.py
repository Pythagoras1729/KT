import os, sys
sys.path.append(os.getcwd())
from collections import OrderedDict
import pandas as pd
import time, subprocess
from Jenkin import jmxeditor, Analyse
from pathlib import Path
import argparse


def Run_test(jmeter_path, jmx_file, result_file, args, Start, End, Step=None):
    '''
    This function performs jmeter test and calls necessary methods to edit the jmx test file and analyses the Test data.
    :param jmeter_path: Location of Jmeter.exe file
    :param jmx_file: Location of Jmeter test file
    :param result_file: Location of Jmeter test output file
    :param args: Input obtained from Jenkins
    '''
    editor.edit_Jmx_File(jmx_file, args, result_file)
    Start, End, Step = Start, End, Step
    while (Start <= End):
        editor.change_Threads(jmx_file, Start)
        start = time.time()
        subprocess.call(r'jmeter -f -n -t {} -l {}'.format(jmx_file, result_file), shell=True,
                        cwd=r'{}'.format(jmeter_path))
        end = time.time()
        runtime = end - start
        analyser = Analyse.Analyse_Result_File(columns=columns, args=args, result_csv=result_file,
                                               runtime=runtime, users=Start)
        if (analyser.check_Latencies()):
            if (Step == None):
                return True
            else:
                Start+=Step
        else:
            if (Step == None):
                return False
            else:
                min=Start//2
                find_sweetspot(jmeter_path=jmeter_path, jmx_file=jmx_file, result_file=result_file, args=args, min=min, max=Start, mid=(Start + min) // 2)
                break
    return analyser.get_Result()


def find_sweetspot(jmeter_path, jmx_file, result_file, args, max, min, mid):
    print(f'Min:{min}, Max:{max}, Mid:{mid}')
    s=0
    if(min==0):
        min=1
    if min < max  and min!=mid :
        # true if test obeys threshold limits
        th_obeyed = Run_test(jmeter_path=jmeter_path, jmx_file=jmx_file, result_file=result_file, args=args, Start=mid,
                             End=max)
        if (th_obeyed):
            s = 1
            print(f'Satisfied threshold limits, s:{s}')
            find_sweetspot(jmeter_path=jmeter_path, jmx_file=jmx_file, result_file=result_file, args=args, max=max,
                           min=mid, mid=(max + mid) // 2)
        else:
            s = 0
            print(f'Failed to satisfy Threshold limits, s:{s}')
            find_sweetspot(jmeter_path=jmeter_path, jmx_file=jmx_file, result_file=result_file, args=args, max=mid,
                           min=min, mid=(mid + min) // 2)
    else:
        if(s==1):
            Run_test(jmeter_path=jmeter_path, jmx_file=jmx_file, result_file=result_file, args=args, Start=max,
                 End=max,Step=max)
        else:
            Run_test(jmeter_path=jmeter_path, jmx_file=jmx_file, result_file=result_file, args=args, Start=min,
                     End=min, Step=min)



if __name__ == "__main__":
    # defining columns for the final output csv file
    columns = OrderedDict()
    st = ['Host', 'URL', 'Method', "e2e_0.50(ms)", "e2e_0.90(ms)", "e2e_0.99(ms)", 'Bottle Neck', 'Test Runtime',
          'Requests sent',
          'response_codes(client expected_response_count)', 'Expected no.of requests sent']
    for i in st:
        columns[i] = []

    # below argparse for argument to be passed as input for details
    PARSER = argparse.ArgumentParser(description='PNS build execution.')
    PARSER.add_argument('-START_RPS', type=int, required=True, help='Starting value to perform test')
    PARSER.add_argument('-STEP_UP_RATE', type=int, required=True, help='Step value')
    PARSER.add_argument('-LOOPS', type=int, required=True, help='No.of loops to perform test')
    PARSER.add_argument('-STOP_RPS', type=int, required=True, help='End value to perform test')
    PARSER.add_argument('-E2E_50_THRESHOLD', type=int, required=True, help='e2e .50 threshold ms')
    PARSER.add_argument('-E2E_90_THRESHOLD', type=int, required=True, help='e2e .90 threshold ms')
    PARSER.add_argument('-E2E_99_THRESHOLD', type=int, required=True, help='e2e .99 threshold ms')
    PARSER.add_argument('-SERVER', type=str, required=True, help='Server to test')
    PARSER.add_argument('-PORT_NUMBER', type=str, required=True, help='Port number')
    PARSER.add_argument('-API_PATH', type=str, required=True, help='path to test')
    PARSER.add_argument('-API_METHOD', type=str, required=True, help='Method GET|POST|PUT')
    ARGS = PARSER.parse_args()
    (START_RPS, STEP_UP_RATE, LOOPS, STOP_RPS) = (ARGS.START_RPS, ARGS.STEP_UP_RATE, ARGS.LOOPS, ARGS.STOP_RPS)
    (SERVER, PORT_NUMBER, API_PATH, API_METHOD) = (ARGS.SERVER, ARGS.PORT_NUMBER, ARGS.API_PATH, ARGS.API_METHOD)

    # Configure  relative paths for local files
    base = Path(__file__)
    jmeter_path = r'{}'.format(str((base / "../jmeter/apache-jmeter-5.2.1/bin").resolve()))
    jmx_file = r'{}'.format(str((base / "../Data/Jmx/testfile.jmx").resolve()))
    result_file = r'{}'.format(str((base / "../Data/CSV/testoutput.csv").resolve()))
    final_out_file = r'{}'.format(str((base / "../Data/CSV/Aggregate_Result.csv").resolve()))

    editor = jmxeditor.Jmx_Editor()
    data = Run_test(jmeter_path=jmeter_path, jmx_file=jmx_file, result_file=result_file, args=ARGS,
                    Start=ARGS.START_RPS, Step=ARGS.STEP_UP_RATE, End=ARGS.STOP_RPS)
    df = pd.DataFrame(data)
    df.to_csv(r'{}'.format(final_out_file), index=False)
