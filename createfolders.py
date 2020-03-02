# Code loops through unique list of names and creates empty folders with the names
import pandas as pd
import os

df = pd.read_csv('/Users/sierraflanagan/Documents/AKFiles/foldernames.csv')
total_indeces = df['customer_id'].size

foldernames = 'customer_id' #column heading of folder names

def main():
    for i in range(total_indeces):
        foldername = df.at[i, foldernames]
        os.mkdir(foldername)

main()
