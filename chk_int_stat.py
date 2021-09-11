#A simple script that will telnet into a router and check that stat of a single
#interface using string formatting


import telnetlib
import time as tm

HOST = "192.168.1.143"
USERNAME = "cisco"
PASSWORD = "cisco"

ENABLE_SECRET = "cisco"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(USERNAME.encode('ascii') + b"\n")

if PASSWORD:
    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode('ascii') + b"\n")

tn.write(b"en\n")
tn.write(ENABLE_SECRET.encode('ascii') + b"\n")
tn.write(b"sh ip int f0/1\n" + b" ")
tm.sleep(1)
data = tn.read_very_eager().decode("ascii")

if data[40:61] == "FastEthernet0/1 is up":
    print("The interface is up")
else:
    print("The interface is down")

    