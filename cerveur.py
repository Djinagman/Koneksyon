import socket 
import threading

sc = True
#ms = True

host , port = ("localhost" , 6666)
sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

sock.bind((host , port))
sock.listen()
print("serveur lanse")

'''
while True:
 
'''
f = input("ext: ")
if f == "Q":
   sc = False

def Multi(c):
  
 
  while True:

    data = c.recv(1024)
    print("client: " ,  data.decode("utf-8"))
    f = input("ext: ")
    if f == "ext":
       break
  
  c.close()

while sc:

  conn , add = sock.accept()   
  Multi(conn)
  fm = input('ext2')
  if fm == "Q":
     sc = False 
 

sock.close()    