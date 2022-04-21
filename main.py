from modules.leaksfinder import LeaksFinder
from modules.internet import Internet 
from modules.darknet import DarkNet
from modules.scatter import ScatterSecrets
from modules.database import Database
# from breachchecker import BreachChecker
from modules.breachdir import BreachDir
from modules.gui import GUI
from modules.validateinput import CheckinputType

# countries: Egypt, Cameroon, Algeria   
# window = GUI()

key = 'mitnick@gmail.com'

KeyType = CheckinputType(key)
parent = LeaksFinder(key, KeyType)

ScatterFinder = ScatterSecrets()
DatabaseFinder = Database()
BreachDirFinder = BreachDir()


DarkFinder = DarkNet()

BreachDirFinder.Search()
DarkFinder.Search()
print(BreachDirFinder.GetResult)
print('_____________________________________________')
print(BreachDirFinder.GetResult)