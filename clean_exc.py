import pandas as pd
import numpy as np

desired_width=400
pd.set_option('display.width',desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

prod_info=pd.read_csv('scraped_info.csv',names=['Product_title','Price','Seller','Rated','Link'])
spec_chars=['Rating','+']
for char in spec_chars:
    prod_info['Rated']=prod_info['Rated'].str.replace(char,' ')

print(prod_info.head(10))
prod_info.to_excel('scraped_info125.xlsx',index=False)