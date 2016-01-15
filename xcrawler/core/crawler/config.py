
from requests import Session


class Config(object):
    """A configuration of a crawler.
    
    Attributes:
        output_file_name (str): the name of an output file.
        output_mode (str): the output mode of a crawler.
        number_of_threads (int): the number of threads used to fetch web pages.
        fetch_delay (float): idle time of a thread in seconds after receiving a response from a server
            and before sending a next request to a server.
        session (requests.Session): a session that specifies shared parameters of requests sent to a server.
    """
    
    OUTPUT_MODE_FILE = 'FILE'
    OUTPUT_MODE_PRINT = 'PRINT'
    OUTPUT_MODE_NONE = 'NONE'
    
    def __init__(self):
        self.output_file_name = "xcrawler_output.csv"
        self.__output_mode = Config.OUTPUT_MODE_FILE
        self.number_of_threads = 3
        self.fetch_delay = 0
        self.session = Session()

    @property
    def output_mode(self):
        return self.__output_mode
    
    @output_mode.setter
    def output_mode(self, value):
        if value in [Config.OUTPUT_MODE_PRINT, Config.OUTPUT_MODE_FILE,
                     Config.OUTPUT_MODE_NONE]:      
            self.__output_mode = value

