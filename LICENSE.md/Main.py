import sys
from Httpc import *

while(True):
    try:
       command = sys.stdin.readline().split()
       command_process(command)
       
    except BaseException as error:
        print(error)




"""
client = Host("httpbin.org", 80)

URL_1 = "/get?course=networking&assignment=1"

client.http_get_request(URL_1, False)
"""
