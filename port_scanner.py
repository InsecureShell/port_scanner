import socket

'''
takes the port number and target and attempts a connection on that port
returns true if a connection is successful
'''
def port_scan(port, target, sock):
    try:
        connection = sock.connect((target, port))
        return True
    except:
        return False

'''
the main part of the program that handles user input and output
'''
def main():
    # create a new INET TCP socket to use
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    target = input("Insert the address of the server to scan: ")

    beginning_port = input("Enter the first port in the port range: ")

    end_port = input("Enter the last port in the port range: ")

if __name__ == '__main__':
    main()
