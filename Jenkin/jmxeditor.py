import xml.etree.ElementTree as etree
class Jmx_Editor():
    def edit_Jmx_File(self,testfile, args,result_file):
        """
        This method edits the jmx file as per client data.
        :param testfile: jmx file which is used to perform Load test.
        :param args: Input Data obtained from Jenkins
        :param result_file: file where jmx test output data has to be stored
        """
        tree = etree.parse(testfile)
        root = tree.getroot()
        for tg in root.iter():
            if ('name' in tg.attrib):
                if tg.attrib['name'] == "LoopController.loops":
                    tg.text = str(args.LOOPS)
                if tg.attrib['name'] == "HTTPSampler.domain":
                    tg.text = str(args.SERVER)
                if tg.attrib['name'] == "HTTPSampler.path":
                    tg.text = str(args.API_PATH)
                if tg.attrib['name'] == "HTTPSampler.protocol":
                    tg.text = 'https'
                if tg.attrib['name'] == "HTTPSampler.port":
                    port = args.PORT_NUMBER
                    if str(port) == 'N/A':
                        tg.text = ''
                    else:
                        tg.text = str(port)
                if tg.attrib['name'] == "HTTPSampler.method":
                    tg.text = args.API_METHOD
                if tg.attrib['name'] =="filename":
                    tg.text=result_file
        tree.write(testfile)
    def change_Threads(self,testfile,threads):
        """
        This methods updates the number of threads in jmx file in accordance with Jenkins data.
        :param testfile: jmx file which is used to perform Load test
        :param threads: No.of users/threads
        """
        tree = etree.parse(testfile)
        root = tree.getroot()
        for tg in root.iter():
            if ('name' in tg.attrib):
                if tg.attrib['name'] == "ThreadGroup.num_threads":
                    tg.text = str(threads)
        tree.write(testfile)

if __name__ =="__main__":
    pass


