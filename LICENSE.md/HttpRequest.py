from Host import *
from Url import *
import re

class HttpRequest:

    __method = "GET"
    __httpVersion = "1.1"
    __requestHeaders = {}        # "{}" - python dictionary
    __requestBody = ""
    __requestURL = ""
    __verbose = False
    __outputFilePath = None
    
    def __init__(self, args):

        #format:   httpc   (get|post)     [-v]    (-h 'k:v')*    [-d inline-data]      [-f file]         [-o outputfile]       URL
        regex = r"(httpc)\s+(post|get)\s+(-v\s+)?(-h\s+(\S+)\s+)*(-d\s+(\'.+?\')\s+)?(-f\s+(\'.+?\')\s+)?(-o\s+(\'.+?\')\s+)?(\'.+?\')"
        match = re.search(regex, args)

        if not match:
            raise LookupError("Unable to format args into a request line")  # Need to learn LoopupError()

        httpc = match.group(1)
        method = match.group(2).upper()
        isVerbose = match.group(3) is not None  # return boolean true or false
        isHeader = match.group(4)

        isData = match.group(6) is not None     # return boolean true or false
        inlineData = match.group(7)

        isFile = match.group(8) is not None     # return boolean true or false
        filePath = match.group(9)

        if(method == 'GET' and (isFile or isData)):
            raise LookupError("Cannot use -d or -f for a GET request")

        if(isFile and isData):
            raise LookupError("Cannot use -d and -f for a POST request")

        outputFile = match.group(10)
        outputFilePath = match.group(11)
        url = match.group(12)

        self.setMethod(method)
        self.setURL(url[1:-1])
        self.__verbose = isVerbose

        if (isHeader):
            regex = r"-h\s+(\'.+?\')\s+"
            headerData = re.findall(regex, args)

            for headerLine in headerData:
                header = headerLine[1:-1].split(':')
                self.addHeader(header[0],header[1])

        if(isData):
            self.addHeader("Content-Length", len(inlineData))
            self.setBody(inlineData)

        if(isFile):
            with open(filePath[1:-1], 'r') as file:
                fileContent = file.read()
                self.addHeader("Content-Length", len(fcontent))
                self.setBody(fileContent)

        if outputFile is not None:
            self.__outputFilePath = outputFilePath[1:-1]



    def buildRequest(self):
        
        hostUrl = Url(self.__requestURL)
        
        requestLine = "{0} {1} HTTP/{2}".format(self.getMethod(), hostUrl.getPath() + hostUrl.getQuery(), self.getHttpVersion())
        
        self.addHeader("Host", hostUrl.getHost())
        
        fullRequest = "{0}\r\n{1}\r\n{2}".format(requestLine, self.getHeaders(), self.getBody())


       # print("fullRequest: \r\n" + fullRequest)
        
        hostObj = Host(hostUrl.getHost(), hostUrl.getPort(), fullRequest, self.__verbose, self.__outputFilePath)
        

        return hostObj


    def addHeader(self, key, value):
        self.__requestHeaders.update({str(key):str(value)})
        

    def getHttpVersion(self):
        return self.__httpVersion

    
    def getHeaders(self):
        allHeaders = ""

        for key in self.__requestHeaders.keys():
            allHeaders += "{0}: {1}\r\n".format(key, self.__requestHeaders.get(key))

        return allHeaders


    def setMethod(self, requestMethod):
        requestMethod = requestMethod.upper()

        if (requestMethod == "GET" or requestMethod == "POST"):
            self.__method = requestMethod
        else:
            print(requestMethod + "is non-defined method")


    def getMethod(self):
        return self.__method

    
    def setBody(self, body):
        self.__requestBody = body


    def getBody(self):
        return self.__requestBody


    def setURL(self, url):
        self.__requestURL = url


    def getURL(self):
        return self.__requestURL
    
        






