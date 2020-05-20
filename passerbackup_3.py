import os
import socket
from binaryornot.check import is_binary
import time
import sys

path = "G:/Proyectos/BackupManager/files/"
ip = "192.168.1.33"
minutos = 5
segundos = minutos*60
loop = sys.argv.pop()

while True:
    files = os.listdir(path)

    for file in files:
        so = socket.socket()
        so.connect((ip,8444))
        print(file)
        so.send(bytes(file,"utf-8"))
        time.sleep(0.1)
        if not is_binary(path+file):
            so.send(bytes("txt","utf-8"))
            pfile = open(path+file,"r")
            fcontent = pfile.read()
            for byte in fcontent:
                print(byte)
                so.send(bytes(byte,"utf-8"))
            so.send(bytes("end","utf-8"))
        else:
            so.send(bytes("bin","utf-8"))
            pfile = open(path+file,"rb")
            fcontent = pfile.read()
            so.sendall(fcontent)
            time.sleep(0.5)
            so.send(bytes("end","utf-8"))
        pfile.close()
        so.close()
    if loop  == "noloop":
        break
    time.sleep(segundos)
    