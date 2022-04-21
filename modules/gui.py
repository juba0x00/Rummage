# Omar Ameer 
# class methods: 
# StartUI

# class attributes:
# SearchLevel
from ttkthemes import ThemedTk
class GUI(ThemedTk):
    def __init__(self):
        super().__init__()

        self.Themes = [
            'adapta', 'alt', 'aquativo', 'arc', 'breeze', 'black', 'blue', 'clam', 'classic', 'clearlooks',
            'default',
            'equilux', 'itft1', 'keramik', 'keramik_alt', 'kroc', 'plastik', 'radiance', 'scidblue',
            'scidgreen',
            'scidgrey', 'scidmint', 'scidpink', 'scidpurple', 'scidsand', 'smog', 'winxpblue', 'yaru'
            ]
        self.theme = self.Themes[18]
        self.mainloop()
