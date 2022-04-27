#!/usr/bin/env python3
from modules.search import Search
from modules.leaksfinder import LeaksFinder
# countries: Egypt, Cameroon, Algeria,  Austria,  Bahrain,  Belgium, Canada,  China, Cameroon, ShittyIsrael
from modules.validateinput import CheckinputType
import datetime
from threading import Thread
from os import system
from pyfiglet import figlet_format 
# from subprocess import Popen, PIPE

# process = Popen('tor', stdout=PIPE, stderr=PIPE)

# stdout, stderr = process.communicate()


SEP = "\033[95m___________________________________________\033[0m"

RED = '\033[31m'
RESET = '\033[0m'
MAGENTA = '\033[35m'
YELLOW = '\033[33m'
UNDERLINE = '\033[4m'
GREEN = '\033[32m'
BOLD = '\033[1m'
print( RED + BOLD + figlet_format('Rummage'))

SearchKey = input(GREEN + BOLD + 'Enter Your Search Key: ' + RESET)


print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

Finder = Search()
Finder.Search(SearchKey)
print(SEP)

sources = LeaksFinder.GetSources()

if len(sources) > 3:
    print(MAGENTA + "Sources: \n" + sources + RESET)

print(RED + BOLD + LeaksFinder.GetResult() + RESET)

print(BOLD + YELLOW + 'Risk Level -> {} {}'.format(LeaksFinder.GetRiskLevel(), RESET))

print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))




# TODO GUI
# ! TODO PROBLEM Visa.db  @HAWASH 
# TODO Organize the code  @HAWASH 
# TODO unique all network classes into one class 


