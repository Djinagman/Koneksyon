import socket 

ent = True

host , pot = ("localhost" , 6666)

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

sock.connect((host , pot))

while ent:
     try:

        msg = input("speak>: ")
        if msg == 'ext':
            ent = False
        msg = msg.encode("utf-8")
        sock.sendall(msg)

     except:
        print("client dekonekte")        

sock.close()