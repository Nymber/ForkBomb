import socket,settings,os, os.path
from os import path
IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
class client():
    def __init__(self):
        parent_dir = ["C:/","C:/Forkbomb_Data"]
        directory = ['Forkbomb_Data','sys','bank','security','user_data']
        y = 0
        fCheck = [False,False,False,False,False]
        for x in range(len(directory)):
            try:
                if x >= 1:
                    y = 1
                else:
                    y = 0
                self.CLIENT_DATA_PATH =  os.path.join(parent_dir[y], directory[x])
                os.makedirs(self.CLIENT_DATA_PATH, exist_ok = True)
                fCheck[x] = str(path.isdir(self.CLIENT_DATA_PATH))
                print("Directory '%s' created successfully" % directory[x] + " [" +str(fCheck[x])+ "]")
            except OSError as error:
                fCheck[x] = False
                print("Directory '%s' can not be created" % directory)
        print(fCheck)
        client.main(self)
    
    def main(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        while True:
            data = client.recv(SIZE).decode(FORMAT)
            cmd, msg = data.split("@")

            if cmd == "DISCONNECTED":
                print(f"[SERVER]: {msg}")
                break
            elif cmd == "OK":
                print(f"{msg}")

            data = input("> ")
            data = data.split(" ")
            cmd = data[0]

            if cmd == "HELP":
                client.send(cmd.encode(FORMAT))
            elif cmd == "LOGOUT":
                client.send(cmd.encode(FORMAT))
                break
            elif cmd == "LIST":
                client.send(cmd.encode(FORMAT))
            elif cmd == "DELETE":
                client.send(f"{cmd}@{data[1]}".encode(FORMAT))
            elif cmd == "UPLOAD":
                path = data[1]

                with open(f"{path}", "r") as f:
                    text = f.read()

                filename = path.split("/")[-1]
                send_data = f"{cmd}@{filename}@{text}"
                client.send(send_data.encode(FORMAT))

        print("Disconnected from the server.")
        client.close()
client()