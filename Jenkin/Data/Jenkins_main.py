from collections import OrderedDict
import pandas as pd
import time,subprocess
from Generic import jmxeditor, Analyse
import argparse

def Run_test(jmeter_path,jmx_file,result_file,client_df):
    for i in range(len(client_df)):
        editor.edit_Jmx_File(jmx_file,client_df,i)
        Start,End,Step=client_df['Start_Point'][i],client_df['End_Limit'][i],client_df['Step_Up_Rate'][i]
        while (Start<=End):
            editor.change_Threads(jmx_file,Start)
            start = time.time()
            subprocess.call(r'jmeter -f -n -t {} -l {}'.format(jmx_file, result_file), shell=True,cwd=r'{}'.format(jmeter_path))
            end = time.time()
            runtime = end-start
            analyser = Analyse.Analyse_Result_File(columns=columns, client_df=client_df, result_csv=result_file, runtime=runtime, users=Start, client_data=i)
            Start += client_df['Step_Up_Rate'][i]
    return analyser.get_Result()

if __name__ == "__main__":
    columns = OrderedDict()
    st = ['Host', 'URL', 'Method', 'Success Rate', "e2e_0.50(ms)", "e2e_0.90(ms)", "e2e_0.99(ms)",'Test Runtime','Requests sent',
          'response_codes(client exptd_response_count)', 'Expected no.of requests sent']
    for i in st:
        columns[i] = []
    # below argparse for argument to be passed as input for details
    PARSER = argparse.ArgumentParser(description='PNS build execution.')
    PARSER.add_argument('-START_RPS', type=int, required=True, help='Starting value to perform test')
    PARSER.add_argument('-STEP_UP_RATE', type=int, required=True, help='Step value')
    PARSER.add_argument('-LOOPS', type=int, required=True, help='No.of loops to perform test')
    PARSER.add_argument('-STOP_RPS', type=int, required=True, help='End value to perform test')
    PARSER.add_argument('-SERVER', type=str, required=True, help='Server to test')
    PARSER.add_argument('-PORT_NUMBER', type=int, required=True, help='Port number')
    PARSER.add_argument('-API_PATH', type=str, required=True, help='path to test')
    PARSER.add_argument('-API_METHOD', type=str, required=True, help='Method GET|POST|PUT')
    ARGS = PARSER.parse_args()
    (START_RPS, STEP_UP_RATE, LOOPS, STOP_RPS) = (ARGS.START_RPS, ARGS.STEP_UP_RATE, ARGS.LOOPS, ARGS.STOP_RPS)
    (SERVER, PORT_NUMBER, API_PATH, API_METHOD) = (ARGS.SERVER, ARGS.PORT_NUMBER, ARGS.API_PATH, ARGS.API_METHOD)
    jmeter_path=r'C:\rbejawad\jmeter\apache-jmeter-5.2.1\bin'
    jmx_file = r'C:\Users\rbejawad\Desktop\KT\Generic\Data\Jmx\testfile.jmx'
    client_file= r'C:\Users\rbejawad\Desktop\KT\Generic\Data\CSV\client_file.csv'
    result_file= r'C:\Users\rbejawad\Desktop\KT\Generic\Data\CSV\testoutput.csv'
    editor = jmxeditor.Jmx_Editor()
    client_df=editor.read_Client_File(client_file)
    data = Run_test(jmeter_path=jmeter_path,jmx_file=jmx_file,result_file=result_file,client_df=client_df)
    df = pd.DataFrame(data)
    df.to_csv(r'C:\Users\rbejawad\Desktop\KT\Generic\Data\CSV\csvout.csv', index=False)
