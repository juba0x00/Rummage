#!/usr/bin/env python3
from sys import argv
from modules.search import Search
from modules.leaksfinder import LeaksFinder
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


TorThread = Thread(target=system('tor >/dev/null 2>/dev/null'))  # ! HANDLE ME
TorThread.start()

if len(argv) == 2:
    SearchKey = argv[1]

    Finder = Search()
    Finder.Search(SearchKey)

    sources = LeaksFinder.GetSources()

    print(LeaksFinder.GetResult())
    print(sources)
else: 
    pass
