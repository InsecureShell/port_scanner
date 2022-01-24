import socket


def port_scan(port, target, sock):
    try:
        connection = sock.connect((target, port))
        return True
    except:
        return False


def main():
    pass


if __name__ == '__main__':
    main()
