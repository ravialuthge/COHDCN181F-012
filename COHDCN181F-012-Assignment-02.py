import socket                                      
import sys,os                                         
from threading import Thread        
                   
                                                                         #.\COHDCN181F-012-Assignment-02.py -l 127.0.0.1 8000

def ser_Architecture():

	 if len(sys.argv) == 4:

            server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            try:
                server_socket.bind((str(sys.argv[2]),int(sys.argv[3])))

            except socket.error :
                print("invalid")
                

            server_socket.listen()
            conection , addr=server_socket.accept()
            
            t2=Thread(target= massage , args=(conection,))
            t2.start()
            
            while True:
                try:
                    send=input()
                    conection.send(send.encode("utf-8")) 
                    if not send:
                        conection.send(" ".encode("utf-8"))
            
                    
                except KeyboardInterrupt:
                    conection.close()
                    sys.exit()
        


def cli_Architecture():
    if len(sys.argv) == 3:
   
            client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            try:
                client_socket.connect((str(sys.argv[1]) ,int(sys.argv[2])))

            except socket.error:
                print("invalid")

            t1=Thread(target= massage , args=(client_socket,))
            t1.start()

            while True:
                try:
                    send=input()
                    client_socket.send(send.encode("utf-8"))
                    if not send:
                        client_socket.send(" ".encode("utf-8"))  
                    

                except KeyboardInterrupt:
                    client_socket.close()
                    sys.exit()
    else:
           print("invalid command")

              
                    
def massage(conection):     

 try:
    while True:
        
            data=conection.recv(2048)
            print(data.decode("utf-8"))

 except KeyboardInterrupt:           
            conection.close()
            sys.exit()
    
ser_Architecture()
cli_Architecture()