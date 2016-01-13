
from requests import Request


class RequestFactory(object):
    """Creates a request sent to a web server.

    """
    def __init__(self):
        pass

    def create_request(self, method, url):
        request = Request(method, url)
        return request