import socket
import re

class Host:

    __connection = None
    __verbose = False
    __httpRequest = None
    __outputFilePath = None

    
    def __init__(self, host, port, message, verbose = False, outputFilePath = None):

        self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.__connection.connect((host, port))

        self.__verbose = verbose
        self.__httpRequest = message
        self.__outputFilePath = outputFilePath

        
    def sendHttpRequest(self):
        self.__connection.send(self.__httpRequest.encode("utf-8"))


    def receiveHttpResponse(self):

        responseLine = self.__connection.recv(1024, socket.MSG_WAITALL)
        httpResponse = responseLine

        while(len(responseLine) > 0):
            responseLine = self.__connection.recv(1024, socket.MSG_WAITALL)
            httpResponse += responseLine

        httpResponse = httpResponse.decode("utf-8")

        splitResponse = httpResponse.split("\r\n\r\n")

        headerPart = splitResponse[0]
        bodyPart = splitResponse[1]

        # redirection detection
        regex = r"HTTP\/1.1\s30[012]"
        match = re.search(regex, headerPart)

        if (match):
            regex = r"Location: (.+)"
            match = re.search(regex, headerPart)

            newUrl = match.group(1)
            return newUrl

        # if verbose set true, print the header part
        if (self.__verbose):
            print(headerPart)

        print(bodyPart)

        if (self.__outputFilePath is not None):
            fs = open(self.__outputFilePath, "w")
            fs.write(headerPart)
            fs.write("\r\n")
            fs.write(bodyPart)
            fs.close()

        self.__connection.close()

        return None






        
