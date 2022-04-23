from modules.search import Search
from modules.leaksfinder import LeaksFinder
# countries: Egypt, Cameroon, Algeria,  Austria,  Bahrain,  Belgium, Canada,  China, Cameroon, ShittyIsrael
from modules.validateinput import CheckinputType
import datetime
from threading import Thread
from os import system
RED = '\033[31m'
RESET = '\033[0m'
MAGENTA = '\033[35m'

# TorThread = Thread(target=system('tor &'))
# TorThread.start()

now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))

key = 'mitnick@gmail.com'
# TorThread.join()
Finder = Search()
Finder.Search(key)
src = LeaksFinder.GetSources()
res = LeaksFinder.GetResult()
print(MAGENTA + src + RESET)
print(RED + res + RESET)

now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))
# TODO GUI 
# TODO show sources
# TODO insert history
# TODO print Risk level 
# TODO database 
    # TODO directory 
