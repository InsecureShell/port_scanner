import socket

'''
takes the port number and target and attempts a connection on that port
returns true if a connection is successful
'''
def port_scan(port, target, sock):
    try:
        sock.connect((target, port))
        return True
    except Exception as e:
        print(e)
        return False

'''
the main part of the program that handles user input and output
'''
def main():

    # get target and port info from user
    target = input("Enter the address of the server to scan: ")

    beginning_port = int(input("Enter the first port in the port range: "))

    end_port = int(input("Enter the last port in the port range: "))

    # scan each port and try to connect to it to see if it's open
    for port in range(beginning_port, end_port):
        # create a new INET TCP socket to use
        # need to make a new one with each loop to connect to each port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if port_scan(port, target, sock):
            print("Port ", port, " is open")


if __name__ == '__main__':
    main()
