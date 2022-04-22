from modules.search import Search
from modules.gui import GUI 
from modules.leaksfinder import LeaksFinder
# countries: Egypt, Cameroon, Algeria   
window = GUI()

key = 'mitnick@gmail.com'

Finder = Search()
Finder.StartSearch(key)
parent = LeaksFinder()

print(parent.GetResult)
# TODO connect classes 
# TODO database payleaks 
# TODO GUI 
# TODO increase level ase level 