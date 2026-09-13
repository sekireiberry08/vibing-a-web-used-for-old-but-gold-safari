import socket
from threading import Thread


def new_connection(conn, addr):
    # print(addr)
    try:
        msg = conn.recv(1024).decode('utf-8')
        if msg: print(f"Recieved from {addr}: {msg}")
        req = "Server responses: " + msg
        conn.send(req.encode('utf-8'))
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

def get_host_default_interface_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
       s.connect(('8.8.8.8',1))
       ip = s.getsockname()[0]
    except Exception:
       ip = '127.0.0.1'
    finally:
       s.close()
    return ip


def server_program(host, port):
    serversocket = socket.socket()
    serversocket.bind((host, port))

    serversocket.listen(10)
    while True:
        conn, addr = serversocket.accept()
        nconn = Thread(target=new_connection, args=(conn, addr))
        nconn.start()

if __name__ == "__main__":
    #hostname = socket.gethostname()
    hostip = get_host_default_interface_ip()
    port = 22236
    print("Listening on: {}:{}".format(hostip,port))
    server_program(hostip, port)
