from collections import Counter
import pandas as pd
class Analyse_Result_File():
    def __init__(self, columns, client_df, result_csv, runtime, users, client_data):
        self.dict = columns
        self.Expected_threads=users
        self.client_df = client_df
        self.client_data = client_data
        self.df = pd.read_csv(result_csv)
        self.test_runtime = str(int(runtime // 60)) + 'min' + ' ' + str(int(runtime % 60)) + 'sec'
        self.dict['Host'].append(self.get_Host())
        self.dict['URL'].append('https://' + str(self.client_df['Server_Name'][client_data]) + str(self.client_df['Path'][client_data]))
        self.dict['Method'].append(self.client_df['Method'][client_data])
        self.Success_Rate = round(self.get_Success_Rate(), 2)
        self.Success_rate = str(self.Success_Rate * 100) + '%'
        self.dict['Success Rate'].append(self.Success_rate)
        percentiles = self.get_Latencies()
        for i in percentiles:
            self.dict[i].append(percentiles[i])
        self.dict['Test Runtime'].append(self.test_runtime)
        self.dict['Requests sent'].append(self.Expected_threads)
        self.dict['response_codes(client exptd_response_count)'].append(self.get_Response_Codes())
        self.dict['Expected no.of requests sent'].append(self.Expected_threads)

    def get_Latencies(self):
        """
        This method returns the Latency metrics for .50, .90 and .99 percentiles from dataframe(csv file)
           """
        percentiles = {}
        percentiles["e2e_0.50(ms)"] = self.df['Latency'].quantile(0.50)
        percentiles["e2e_0.90(ms)"] = round(self.df['Latency'].quantile(0.90), 0)
        percentiles["e2e_0.99(ms)"] = round(self.df['Latency'].quantile(0.99), 0)
        return percentiles
    def get_Host(self):
        """
        This method returns Host name from dataframe(csv file)
            """
        return self.df['Hostname'][0]
    def get_Success_Rate(self):
        """
        This method returns the percentage of threads whose requests succeeded, from dataframe(csv file)
            """
        c = 0
        for i in self.df['responseMessage']:
            if (i == 'OK'):
                c += 1
        Success_Rate = c / len(self.df['responseMessage'])
        return Success_Rate
    def get_Response_Codes(self):
        """
        This method returns the various response codes obtained during the load test, from dataframe(csvfile)
            """
        dict2 = Counter(self.df['responseCode'])
        l = []
        for i in dict2:
            l.append('{ ' + str(i) + " : " + str(dict2[i]) + " }")
        s=', '.join(l)
        return s
    def get_Result(self):
        """
         This method returns the aggregate results of the load test performed, from dataframe(csv file)
            """
        return self.dict

if __name__ == "__main__":
    pass