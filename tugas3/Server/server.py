import socket 
from threading import Thread 


class SendingThread(Thread) :
    def __init__(self, addr, sock, filetosend,count):
        Thread.__init__(self) 
        self.sock = sock
        self.target = addr
        self.file = filetosend
        print "[+] server created for "+ str(addr)
        
    def run (self):
        
        print "[.] begin sending "+ self.file + "to " + str(self.target)
        self.sock.sendto("#start", self.target)
        self.sock.sendto(self.file, self.target)
        fp = open(self.file, 'rb')
        payload = fp.read()
        for byte in payload:
            self.sock.sendto(byte, self.target)
        
        self.sock.sendto("##EOF", self.target)
        print "[-] finish sending "+ self.file + "to " + str(self.target)
        
        
        
class Server():
    def __init__(self):
        socketbind = 9000
        ip = "127.0.0.1"
        
        self.socketbind = (ip, socketbind)
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(self.socketbind)
        self.clientList = []
        self.imagelist = ["1.jpg"]
        for a in self.imagelist:
           self.count = 0
        



    def loop (self):
	flag=0
        while (True):
            data, addr = self.sock.recvfrom(1024)
            
            if data == "#ask":  
                data, addr = self.sock.recvfrom(1024)
                fileasked = self.imagelist[int(data)-1];
                
                newthread = SendingThread(addr, self.sock, fileasked,self.count)
                newthread.start()
                self.count +=1
                flag+=1
            if(flag==1):
                data="#end"

if __name__ == "__main__":
    main = Server()
    main.loop()