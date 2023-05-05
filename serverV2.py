from blockchain import Blockchain
import json
import socket

blockchain = Blockchain()

host = ''
port = 2034

t1 = blockchain.new_data("Tommy Siuuuuuu", "Tommy Scherphorn")
t2 = blockchain.new_data("JP", "Andre")
t3 = blockchain.new_data("Dr. Bayntun", "Patrick")
blockchain.add_block(12)
store_value = str(blockchain.chain)

def setupServer():
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   print("Socket created")
   try:
      s.bind((host,port))
   except socket.error as msg:
      print(msg)
   print("Socket Complete")
   return s

def setupConnection():
   s.listen(1) 
   conn, address = s.accept()
   print("Connected to: " + address[0] + ":" + str(address[1]))
   return conn


def get(input, input2):
   t4 = blockchain.new_data(input, input2)
   blockchain.add_block(15)
   reply = str(blockchain.chain)
   return reply

def dataTransfer(conn):
   data = conn.recv(1024)  # receive the data
   data = data.decode('utf-8')
   print(data)

   dataMessage = data.split(' ', 1)
   command = dataMessage[0]
   name = dataMessage[1]
   print(command)
   if command == 'KILL':
        print('Our server is shutting down')
        s.close()
   else:
        reply = get(command, name)
   conn.sendall(str.encode(reply))
   print("Data has been sent!")
   conn.close()

s = setupServer()

while True:
   try:
      conn = setupConnection()
      dataTransfer(conn) 
   except:
      break
