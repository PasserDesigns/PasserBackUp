import socket
import datetime
import os

so = socket.socket()
so.bind(("0.0.0.0", 8444))
so.listen()

while True:
    con, addr = so.accept()
    time = datetime.datetime.now()
    path = time.strftime("G:/Proyectos/BackupManager/backup/%Y%m%d%H/")
    if not os.path.isdir(path):
        os.mkdir(path)
        print(path+" creado.")
    nfile = con.recv(1024).decode()
    print(nfile)
    tfile = con.recv(1024).decode()
    if tfile == "txt":
        pfile = open(path+nfile, "w")
        while True:
            temp = con.recv(1024)
            if temp.decode() == "end":
                print("end")
                con.close()
                pfile.close()
                break
            else:
                pfile.write(temp.decode())
    elif tfile == "bin":
        pfile = open(path+nfile, "wb")
        while True:
            temp = con.recv(1024)
            if temp == bytes("end", "utf-8"):
                print("end")
                con.close()
                pfile.close()
                break
            else:
                pfile.write(temp)