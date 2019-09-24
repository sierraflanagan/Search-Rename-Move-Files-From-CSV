import pandas as pd
import shutil
import os

# insert csv file 
df = pd.read_csv('/Users/sierraflanagan/Documents/filemovertest/textfilemover.csv') 
total_indeces = df['old_filename'].size
oldfolder = '/Users/sierraflanagan/Documents/filemovertest/'
old_col = 'old_filename' #column heading of old filenames
new_col = 'new_filename' #column heading of new filenames

def main():
    for i in range(total_indeces):
        oldName = df.at[i, old_col]
        newName = df.at[i, new_col]
        old_ext = find_filepath(oldName, oldfolder)
        print(oldName)
        new_ext = create_new_filepath(newName)
        shutil.move(old_ext, new_ext)

def find_filepath(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root,name)

def create_new_filepath(newname):
    #The new folder where the renamed files will be moved
    newfolder = '/Users/sierraflanagan/Documents/filemovertest/'
    newfilepath = newfolder + newname
    return newfilepath 

main()