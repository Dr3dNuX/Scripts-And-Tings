## this script will telnet into a device and issuse any command you give it
## then will parse though the return output from the telnet command
## and place everyline into a single array element
## once the alorithm finds a line break it places that string into its own element



import telnetlib
import time as tm

def int_command_parser(data):
    command_data = data
    command_out_array = []
    finished_array = []
    string1 = ""

    for char in str(command_data):
        command_out_array.append(char)
        string1 = string1 + char
        if char == "\n":
            finished_array.append(string1)
            string1 = ""
    return finished_array

HOST = "192.168.1.143"
USERNAME = "cisco"
PASSWORD = "cisco"
PADDING = b" " * 10

ENABLE_SECRET = "cisco"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(USERNAME.encode('ascii') + b"\n")

if PASSWORD:
    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode('ascii') + b"\n")

tn.write(b"en\n")
tn.write(ENABLE_SECRET.encode('ascii') + b"\n")
tn.write(b"sh run\n" + PADDING)
tm.sleep(5)
output = tn.read_very_eager().decode("ascii")


finished = int_command_parser(output)

print(finished)