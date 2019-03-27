import socket


class Client:
    def __init__(self):
        socketbind = 9000
        ip = "127.0.0.1"
        self.server = (ip, socketbind)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
   
    def sendMessage(self):
        while (True):
            print "============================"
            print "image list :"
            print "1. 1.jpg"
            print "2. 2.jpg"
            print "3. 3.jpg"
            print "4. 4.jpg"
            print "============================"
            message = raw_input()
            message = message.strip()
            acceptedAnswer = ['1','2','3','4']
            if message in acceptedAnswer :
                flag = 0
                while flag !=1:
                    self.sock.sendto("#ask", self.server)
                    self.sock.sendto(message, self.server)
                    data, addr = self.sock.recvfrom(1024)
                    if (data == "#start"):
                        data, addr = self.sock.recvfrom(1024)
                        filename = data 
                        print ("[+] receiving " + filename + " from " + str(addr))
                        
                        fp = open(data, "wb+")
                        while True:
                            data, addr = self.sock.recvfrom(1024)        
                            if data == "##EOF":
                                print ("[-] received " + filename + " from " + str(addr))
                                fp.close()
                                break
                            fp.write(data)
                    flag+=1    
            else : 
                print "select from following (1,2,3) : "
            #self.sock.sendto(message, self.server)
        

if __name__ == "__main__":
    main = Client()
    main.sendMessage()