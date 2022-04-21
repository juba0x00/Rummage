from leaksfinder import LeaksFinder
from internet import Internet 
from darknet import DarkNet
from scatter import ScatterSecrets
from database import Database
# from breachchecker import BreachChecker
from breachdir import BreachDir
from gui import GUI
from validateinput import CheckinputType

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