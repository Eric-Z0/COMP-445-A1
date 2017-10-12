from HttpRequest import *
from Host import *

def command_process(cmd):

	# Check if the command is an empty string
	if(len(cmd) == 0):
		print("The command line is empty")
		return
	
	# Check if the command first starts with "httpc"
	if(cmd[0] != "httpc"):
		print(cmd[0] + " is not a valid command.")
		return

        # Check if there is any argument given after "httpc"
	if(len(cmd) == 1):
		print("No arguement is given.")
		return
	
	if(cmd[1] == "help"):
		help_menu(cmd)
		
	if(cmd[1] == "get" or cmd[1] == "post"):
                redirectionCtr = 1
                while(True):
                        HostObj = HttpRequest(" ".join(cmd)).buildRequest();
                        HostObj.sendHttpRequest()
                        response = HostObj.receiveHttpResponse()

                        if (response is not None):
                                if(redirectionCtr > 5):
                                        print("Too many redirections.")
                                        return
                                print(str(redirectionCtr) + "- Redirecting to " + response)
                                cmd[-1] = "'" + response + "'"
                                redirectionCtr = redirectionCtr + 1
                        else:
                                break
                return
                        
	print(cmd[1] + " is not a valid command.")

		
def help_menu(arg):
	# When user only enter httpc help
	if(len(arg) == 2):
		print("""
		httpc is a curl-like application but supports HTTP protocol only.
		Usage: 
			httpc command [arguments]
		The commands are: 
		get 	executes a HTTP GET request and prints the response. 
		post 	executes a HTTP POST request and prints the response. 
		help 	prints this screen. 
		
		Use "httpc help [command]" for more information about a command.""")
	else:
		if(arg[2] == "get"):
			print("""
			httpc help get
			usage: httpc get [-v] [-h key:value] URL 
			Get executes a HTTP GET request for a given URL.
				-v 				Prints the detail of the response such as protocol, status, and headers. 
				-h 	key:value 	Associates headers to HTTP Request with the format 'key:value'.""")
		
		elif(arg[2] == "post"):
			print("""
			httpc help post
			usage: httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL Post executes a HTTP POST request for a given URL with inline data or from file.
			
				-v 				Prints the detail of the response such as protocol, status, and headers. 
				-h key:value 	Associates headers to HTTP Request with the format 'key:value'. 
				-d string 		Associates an inline data to the body HTTP POST request. 
				-f file 		Associates the content of a file to the body HTTP POST request. 
			
			Either [-d] or [-f] can be used but not both.""")
		
		else:
			print(arg[2] + " is not a valid httpc command")
		
	
		
		
		
		
		
		
		
		
