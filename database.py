# Omar Khaled 
import pandas as pd
class Databae():
    def __init__(self, InputSearchKey):
        self.__SearchKey = InputSearchKey
        self.__Result: str
         
    def CheckCreditCard(self, SearchKey):
        df = pd.read_excel('PayLeaks.xlsx')
        if(len(SearchKey) == 11):
            return True if SearchKey in str(df.loc[df['PayLeaks'] == SearchKey]) else False
        else:
            #! Show Error Windows "Invalid input" @Omar_Ameer 
            return "invalid input"
        

