import socket                                      
import sys,os                                         
import argparse
from threading import Thread 

p=argparse.ArgumentParser()                              #.\COHDCN181F-012-Assignment-01.py -l 127.0.0.1 8000
p.add_argument("serverip",nargs='?',type=str)            
p.add_argument("-l","--ip",type=str)   
p.add_argument("port",type=int)
args = p.parse_args()

def server():
    if args.ip:
        if args.port:
            
            s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

            try:
                s.bind((args.ip ,args.port))

            except socket.error as e:
                print(str(e))
                

            s.listen()
            conn , addr=s.accept()
            
            t1=Thread(target=msg , args=(conn,))
            t1.start()
            
            while True:
                try:
                    send=input()
                    conn.send(send.encode("utf-8"))
                    
                except KeyboardInterrupt:
                    conn.close()
              
def client():
    if args.serverip:
        if args.port:
            
            c=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

            try:
                c.connect((args.serverip ,args.port))

            except socket.error as e:
                print(str(e))

            t2=Thread(target=msg , args=(c,))
            t2.start()

            while True:
                try:
                    send=input()
                    c.send(send.encode("utf-8"))
                    
                except KeyboardInterrupt:
                    c.close()
                    
def msg(conn):     

    while True:
        
            data=conn.recv(2048)
            print(data.decode("utf-8"))
                        
            if not data:
                break
    
server()
client()
