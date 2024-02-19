import socket
from ipaddress import IPv4Network

#------------------------------------------------
import pyfiglet

def print_big_word(word):
    ascii_art = pyfiglet.figlet_format(word)
    print(ascii_art)

word = "VEXMAN"
print_big_word(word)

#-----------------------------------------------

def scan(target):
  converted_ip = check_ip(target)
  print('\n' + "(0__0) Sacnning the Target  " + str(target))
  for port in range(1,100):
    scan_port(converted_ip,port)
  
def check_ip(ip):
  try:
    IPv4Network(ip)
    return(ip)
  except ValueError:
    return(socket.gethostbyname(ip))

def scan_port(ipaddress,port):
  try:
    sock = socket.socket()
    sock.settimeout(0.3)
    sock.connect((ipaddress,port))
    print("[+] Port Opened: " + str(port))
  except:
    pass

targets = input("[+] Enter Target/s To Scan(Use , in between each target to scan multiple)")
if ',' in targets:
  for ip_add in targets.split(','):
    scan(ip_add.strip(' '))
else:
  scan(targets)

