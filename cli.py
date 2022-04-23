#!/usr/bin/env python3
from modules.search import Search
from modules.leaksfinder import LeaksFinder
# countries: Egypt, Cameroon, Algeria,  Austria,  Bahrain,  Belgium, Canada,  China, Cameroon, ShittyIsrael
from modules.validateinput import CheckinputType
import datetime
from threading import Thread
from os import system
SEP = "\033[95m___________________________________________\033[0m"

RED = '\033[31m'
RESET = '\033[0m'
MAGENTA = '\033[35m'
YELLOW = '\033[33m'
UNDERLINE = '\033[4m'
GREEN = '\033[32m'
BOLD = '\033[1m'

print("""%s
        ____                                             
        |  _ \ _   _ _ __ ___  _ __ ___   __ _  __ _  ___ 
        | |_) | | | | '_ ` _ \| '_ ` _ \ / _` |/ _` |/ _ \
        |  _ <| |_| | | | | | | | | | | | (_| | (_| |  __/
        |_| \_\\__,_|_| |_| |_|_| |_| |_|\__,_|\__, |\___|
                                            |___/      
                                             
                                             
                                             """ % (RED))

SearchKey = input(GREEN + BOLD + 'Enter Your Search Key: ' + RESET)

# TorThread = Thread(target=system('tor >/dev/null 2>/dev/null'))  # ! HANDLE ME
# TorThread.start()
# TorThread.join()

print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

Finder = Search()
Finder.Search(SearchKey)
print(SEP)

sources = LeaksFinder.GetSources()

if len(sources) > 1:
    print(MAGENTA + sources + RESET)

print(RED + BOLD + LeaksFinder.GetResult() + RESET)

print(BOLD + YELLOW + 'risk level -> {} {}'.format(LeaksFinder.GetRiskLevel(), RESET))

print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))




# TODO GUI 
# TODO Start TOR in windows 
# TODO TOR Connection Validation 
# TODO Linux Redirect Tor command output (HANDLE ME flag)
# TODO database 
    # TODO directory hawash 
    # TODO insert history 
    # TODO Last Search > month then don't trust the history 
