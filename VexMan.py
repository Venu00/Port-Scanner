import socket
 
def check_ip(ip):
    try:
        socket.inet_aton(ip)
        return ip
    except socket.error:
        try:
            ip = socket.gethostbyname(ip)
            return ip
        except socket.gaierror:
            print("VEX says Invalid IP address or domain name")
            return None

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.4)
        sock.connect((ipaddress, port))
        print("VEX says the Port " + str(port) + " is open")
        sock.close()
    except Exception as e:
        print("VEX says the Port " + str(port) + " is not open: " + str(e))

ipaddress = input("[~] Enter the Target: ")
converted_ip = check_ip(ipaddress)

if converted_ip:
    for port in range(1, 150):  #Start from 1, end at 100
        scan_port(converted_ip, port)
