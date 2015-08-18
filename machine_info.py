import socket
import hashlib


def get_remote_machine_info():
    host = 'www.ifce.edu.br'
    try:
        print "ip: %s" % socket.gethostbyname(host)
    except socket.error, err_msg:
        print "%s : %s" % (host, err_msg)


def find_service_name():
    proto = 'tcp'
    for port in [1, 2, 3]:
        print "Port: %s => service name: %s" % (port, socket.getservbyport(port, proto))


def get_md5(msg):
    """
    Exibe o hash de uma mensagem de texto
    """
    #h = hashlib.md5()
    #h.update(msg)
    return hashlib.md5(msg).hexdigest()


if __name__ == '__main__':
    #get_remote_machine_info()
    #find_service_name()
    msg = raw_input("Type the secret message: ")
    print "Hash: %s" % get_md5(msg)