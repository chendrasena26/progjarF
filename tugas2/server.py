from threading import Thread
import socket
import os
import time

SERVER_IP="127.0.0.1"
SERVER_PORT = 9000

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

namafile=["Bigchungus.jpg","Bluewill.png","Mafia.png"]

def getRequest():
  while True:
    print "Menunggu request..."
    data,addr=sock.recvfrom(1024)
    data_to_string=str(data)
    if(data_to_string[:3]=="REQ"):
      thread = Thread(target=setImage,args=(addr))
      thread.start()

def setImage(ip,port):
  addr=(ip,port)
  for x in namafile:
    time.sleep(5)
    kirim(x,addr)
  sock.sendto("CLOSE",addr)

def kirim(imgname,addr):
  fp=open(imgname,'rb')
  paket=fp.read()
  terkirim=0
  fp.close()
  sock.sendto(("START "+imgname),addr)
  panjangpkt=len(paket)
  iterasi=(panjangpkt/1024)
  for i in range(iterasi+1):
    data=[]
    if (i+1)*1024 > panjangpkt:
      data = paket[i*1024:panjangpkt]
      terkirim=terkirim+len(data)
    else:
      data=paket[i*1024:(i+1)*1024]
      terkirim=terkirim+len(data)
    sock.sendto(data,addr)
    print "Mengirim "+str(terkirim)+" dari "+str(panjangpkt)
  sock.sendto(("END "+imgname),addr)

while True:
  getRequest()