# Hawash, Bassel, Azab
# Darknet class is a child of internet class 
from internet import Internet 
from os import system
import socks
import socket
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
class DarkNet(Internet):
    def __init__(self):
        super().__init__()
        try:
            system('service tor start || systemctl start tor.service')
        except:
            pass


    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
    socket.socket = socks.socksocket

    def GetAddrInfo(*args):
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

    socket.getaddrinfo = GetAddrInfo



