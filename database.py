# Omar Khaled 
import pandas as pd
class Databae():
    def Check_cridt_card(self, SearchKey):
        df = pd.read_excel('PayLeaks.xlsx')
        if(len(SearchKey) == 11):
            return True if SearchKey in str(df.loc[df['PayLeaks'] == SearchKey]) else False
        else:
            return "invalid input"
