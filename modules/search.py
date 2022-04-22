from modules.leaksfinder import LeaksFinder
from modules.internet import Internet 
from modules.darknet import DarkNet
from modules.scatter import ScatterSecrets
from modules.database import Database
from modules.breachdir import BreachDir
from modules.validateinput import CheckinputType

class Search():
    
    def __init__(self):
    #     self.ScatterFinder = ScatterSecrets()
        self.DbFinder = Database()
        self.BreachDirFinder = BreachDir()
    #     self.DarkFinder = DarkNet()
        
        
    
    
    def StartSearch(self, SearchKey):
        SearchType = CheckinputType(SearchKey)
        print(SearchType)
        LeaksFinder.SetAtrrs(SearchKey, SearchType) 
        
        # self.DbFinder.Search('History')
        
        if SearchType == 'Email':
            # print('start scatter')
            # self.ScatterFinder.Search()
            print(' start breachdir ')
            self.BreachDirFinder.Search()
            print('end breachedir, start darker')
            # self.DarkFinder.Search()
            
        elif SearchType == 'Username':
            self.BreachDirFinder.Search()
            # self.DarkFinder.Search()
            
        elif SearchType == 'PhoneNumber':
            self.DbFinder.Search(Internet.GetCountry)
            
        elif SearchType == 'Visa':
            self.DbFinder.Search('Visa')
        else:
            #! window error 
            pass 