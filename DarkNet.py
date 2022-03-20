# Hawash, Bassel, Azab
# Darknet class is a child of internet class 
from internet import Internet
from os import system
from stem.control import Controller 
class DarkNet(Internet):
    def __init__(self):
        super().__init__()
        try:
            system('service tor start || systemctl start tor.service')
        except:
            pass
        #╭─root@Kubuntu /home/juba 
        #╰─# nmap -sV -p- localhost         
        # Starting Nmap 7.80 ( https://nmap.org ) at 2022-03-20 18:08 EET
        # Nmap scan report for localhost (127.0.0.1)
        # Host is up (0.0000030s latency).
        # Not shown: 65527 closed ports
        # PORT      STATE SERVICE         VERSION
        # 9050/tcp  open  tor-socks       Tor SOCKS proxy
        # 9051/tcp  open  tor-control     Tor control port (Authentication required)

        # with Controller.from_port(port=9051) as controller:
            # # Authenticating to our controller with the password
            # # we used when we used the 'tor --hash-password' command
            # controller.authenticate(password="your Tor password")
            # # Send signal to Tor controller to create new identity
            # # (a new exit node IP)
            # controller.signal(Signal.NEWNYM)


        pass
