testfile.jmx
--Jmx file consisting all the relevant information to start the load testing

testoutput.csv
--Result file generated using jmeter test interface to obtain the aggregate result

Analyse.py
-- The file provides final values of the Jmeter load test result obtained to append in the result file
--Structure
    Class-
    Analyse_Result_File
	Methods-
	    get_Latencies
	        This method returns the Latency metrics for .50, .90 and .99 percentiles from dataframe(csv file)
	    get_Host
	        This method returns Host name from dataframe(csv file)
	    get_Success_Rate
	        This method returns the percentage of threads whose requests succeeded, from dataframe(csv file)
	    get_Response_Codes
	        This method returns the various response codes obtained during the load test, from dataframe(csvfile)
	    get_Result
	        This method returns the aggregate results of the load test performed, from dataframe(csv file)

jmxeditor.py
-- The file edits the jmx file as per client requirement, like changing the values of number of users or webpage on which the testing will be performed
--Structure
    Class-
    JmxEditor
	Methods-
	    edit_Jmx_File
	        This method edits the jmx file as per client data.
        change_Threads
            This methods updates the number of threads in jmx file in accordance with client data.

main.py
--The main file to execute the complete code

csvout.csv
--Final result file that contains the aggregate result of all the individual tests.




