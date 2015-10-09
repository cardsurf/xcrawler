
try:
    from urllib2 import Request
except ImportError:
    from urllib.request import Request


class RequestFactory:
    """Creates a request sent to a web server.

    """

    def __init__(self):
        pass

    def create_request(self, url):
        request = Request(url)
        request.http_header = {'User-Agent': "Urllib Browser"}
        return request