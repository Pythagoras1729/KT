from collections import Counter
import pandas as pd


class Analyse_Result_File():
    def __init__(self, columns, args, result_csv, runtime, users):
        '''
        :param columns: Columns for final output file
        :param args: Input data obtained from Jenkins
        :param result_csv: Csv file obtained after Jmeter test run
        :param runtime: Time taken to complete Jmeter test
        :param users: No.of threads used to perform current test
        '''
        self.dict = columns
        self.Expected_threads = users
        self.args = args
        self.df = pd.read_csv(result_csv)
        self.dict['Host'].append(self.get_Host())
        self.dict['URL'].append('https://' + str(self.args.SERVER) + str(self.args.API_PATH))
        self.dict['Method'].append(self.args.API_METHOD)
        percentiles = self.get_Latencies()
        for i in percentiles:
            self.dict[i].append(percentiles[i])
        self.dict['Test Runtime'].append(str(int(runtime))+'sec')
        self.dict['Requests sent'].append(self.Expected_threads)
        self.dict['Bottle Neck'].append(self.get_Bottle_Neck(self.check_Latencies()))
        self.dict['response_codes(client expected_response_count)'].append(self.get_Response_Codes())
        self.dict['Expected no.of requests sent'].append(self.Expected_threads)

    def check_Latencies(self):
        """
        This method reads the Latency metrics for .50, .90 and .99 percentiles from dataframe(csv file) and compare them with given threshold values
        :return: True or False
            """
        e2e_50_th, e2e_90_th, e2e_99_th = self.args.E2E_50_THRESHOLD, self.args.E2E_90_THRESHOLD, self.args.E2E_99_THRESHOLD
        e2e_50 = self.df['Latency'].quantile(0.50)
        e2e_90 = round(self.df['Latency'].quantile(0.90), 0)
        e2e_99 = round(self.df['Latency'].quantile(0.99), 0)
        return True if ((e2e_50 <= e2e_50_th) and (e2e_90 <= e2e_90_th) and (e2e_99 <= e2e_99_th)) else False

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

    def get_Bottle_Neck(self, bool):
        """
        This method returns the percentage of threads whose requests succeeded, from dataframe(csv file)
            """
        return 'Yes' if bool is False else 'No'

    def get_Response_Codes(self):
        """
        This method returns the various response codes obtained during the load test, from dataframe(csvfile)
            """
        dict2 = Counter(self.df['responseCode'])
        l = []
        for i in dict2:
            l.append('{ ' + str(i) + " : " + str(dict2[i]) + " }")
        s = ', '.join(l)
        return s

    def get_Result(self):
        """
         This method returns the aggregate results of the load test performed, from dataframe(csv file)
            """
        return self.dict


if __name__ == "__main__":
    pass
