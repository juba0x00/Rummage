from attr import validate
from internet import Internet 
from darknet import DarkNet
from scatter import ScatterSecrets
from database import Database
# from breachchecker import BreachChecker
from breachdir import BreachDir
from gui import GUI
from validateinput import CheckinputType
from whatismyip import Whatismyip


# window = GUI()

key = 'mitnick@gmail.com'

KeyType = CheckinputType(key)
parent = Internet(key, KeyType)

ScatterFinder = ScatterSecrets()
DatabaseFinder = Database()
BreachDirFinder = BreachDir()
WhatismyipFinder = Whatismyip()



DarkFinder = DarkNet()

BreachDirFinder.Search()
DarkFinder.Scrape()
print(BreachDirFinder.GetResult)
print('_____________________________________________')
print(BreachDirFinder.GetResult)