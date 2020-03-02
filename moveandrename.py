# File used to search in given folder for filenames in a csv file, rename them and move them to a new folder.

import pandas as pd
import shutil
import os

# insert csv file as pandas dataframe
df = pd.read_csv(#file path to csv file)

#assigning names to columns of dataframe
total_indeces = df['old_names'].size
oldfolder = '/Users/sierraflanagan/Documents/AKFiles/Customers/'
old_col = 'old_names' #column heading of old filenames
new_col = 'new_names' #column heading of new filenames
customerId_col = 'customer_id' 
error_col = 'errornames' #should be blank ... will spit out new excel document and these columns will populate if error thrown

#revisedId_col = 'revised_id' 


#print(type(old_col))
#df.head()

def main():
    for i in range(total_indeces):
        oldName = df.at[i, old_col]
        newName = df.at[i, new_col]
        #oldcustomerId = df.at[i, customerId_col] (these 2 lines added because box name formatting did not support some customer IDs)
        newcustomerId = df.at[i, revisedId_col]
        old_ext = find_filepath(oldName, '/Users/sierraflanagan/Documents/AKFiles/Customers/')
        new_ext = create_new_filepath(newName, newcustomerId)
        if old_ext == None:
            df.at[i, error_col] = oldName
        else:
           # print(new_ext)
            shutil.move(old_ext, new_ext)
        
def find_filepath(name, path):
    for root, dirs, files in os.walk(path, topdown = True):
        if name in files:
            return os.path.join(root,name)

def create_new_filepath(newname, c_id):
    #The new folder where the renamed files will be moved
    newfolder = '/Users/sierraflanagan/Documents/AKFiles/Customers/'
    # Supports folder structure naming convention
    newfilepath = newfolder + c_id + '/' + newname
    return newfilepath 

main()
# creates excel file with names that errored in the 'errornames' column with the name "test1.xlsx"
# Meant to be edited, delete columns that did not error, fix errored names, save as .csv
# then used as input for the next run
df.to_excel('test1.xlsx')
