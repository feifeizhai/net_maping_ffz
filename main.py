import os

import sys, socket, time, threading,queue
from asyncio import async
from time import sleep
import uuid

import other

# 获取本机IP地址




# print(socket.getfqdn(socket.gethostname()))
# mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
# print(":".join([mac[e:e+2] for e in range(0,11,2)]))


# 获取ARP表
# os.system('arp -a > temp.txt')

# with open('temp.txt') as fp:
#
#     for line in fp:
#         print(line)
#         line = line.split()[:2]
oldIp = ''
def searchIp():
  host = socket.gethostbyname_ex(socket.gethostname())

  ips = host[2]
  print(ips)
  for ip in ips:
    if ip != '192.168.2.12':
      print(ip)
      return ip


def startMap(ip):
  print(ip)
  other.startMapping(ip)

if __name__ == '__main__':

  while True:
    newIp = searchIp()
    if oldIp != newIp:
      print(newIp)
      # startMap(newIp)
      print(type(newIp))
      threading.Thread(target=startMap, args=(newIp,)).start()
      oldIp = newIp

    sleep(5)
