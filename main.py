from modules.search import Search
# from modules.gui import GUI 
from modules.leaksfinder import LeaksFinder
# countries: Egypt, Cameroon, Algeria   
# window = GUI()

from modules.leaksfinder import LeaksFinder
from modules.internet import Internet 
from modules.darknet import DarkNet
from modules.scatter import ScatterSecrets
from modules.database import Database
from modules.breachdir import BreachDir
from modules.validateinput import CheckinputType

import datetime
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))

key = 'mitnick@gmail.com'
Finder = Search()
Finder.StartSearch(key)
res = LeaksFinder.GetResult()
status = LeaksFinder.GetStatus()
print(status)
print(res)

now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# TODO connect classes 
# TODO database payleaks 
# TODO GUI 
# TODO increase level ase level 