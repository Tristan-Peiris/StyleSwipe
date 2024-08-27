import socket
from client.net import commandHandeler

runningClient = None # Saves the started client socket object

# Input: ip and port to connect to
# Process: Create a client socket object and connect to the server
# Output: The client socket object
def startClient(ip, port): # Starts client and connects to the server
    global runningClient
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    runningClient = client

# Input: command to be sent to the server
# Process: Encode the command and send it to the server
# Output: Response from the server
def runCommand(command, args): # Sends a command to the server and collects the response
    match command:
        case "get clothing list":
            runningClient.send("get clothing list".encode())
            return runningClient.recv(1024).decode()
        case "upload clothing item":
            commandHandeler.uploadItem(runningClient, args[0], args[1])
