# Osama 
import pandas as pd
class Databae():
    def Check_cridt_card(self,Search_key):
        df = pd.read_excel('PayLeaks.xlsx')
        if(len(Search_key) == 11):
            return df.loc[df['PayLeaks'] == Search_key]
        else:
            return "invalid input"

OPJ=Databae()
print(OPJ.Check_cridt_card("40604-30720"))
