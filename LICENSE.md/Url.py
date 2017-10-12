from urllib.parse import urlparse

class Url:

    # private attributes identified by two underscores
    __scheme = None
    __host = None
    __port = None
    __path = None
    __query = None


    def __init__(self, url):

        urlInfo = urlparse(url)

        self.__scheme = urlInfo.scheme + "://"

        if (urlInfo.hostname == None and urlInfo.port == None):
            self.__scheme = "http://"
            urlInfo = urlparse(self.__scheme + url)

        self.__query = urlInfo.query
        self.__path = urlInfo.path

        if (urlInfo.path == ""):
            self.__path = "/"

        self.__host = urlInfo.hostname

        # Only set the port if there is one
        if not urlInfo.port == None:
            self.__port = urlInfo.port
        else:
            self.__port = 80


    def getScheme(self):
        return self.__schmem


    def getHost(self):
        return self.__host
    

    def getPort(self):
        return self.__port
    

    def getPath(self):
        return self.__path
    

    def getQuery(self):
        return "?" + self.__query
    

    def getFullURL(self):

        FullURL = "{0}{1}{2}".format(self.__scheme, self.__host, self.__path)

        if(self.__query is not ""):
            FullURL += "?{0}".format(self.__query)

        return FullURL



    
    
