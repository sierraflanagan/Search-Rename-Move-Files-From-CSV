import pandas as pd
import shutil
import os

# insert csv file 
# Load CSV with columns of old filenames and new filenames as pandas dataframe
df = pd.read_csv('/Users/sierraflanagan/Documents/filemovertest/textfilemover.csv') 
# Get amount of files, to be used to iterate
total_indeces = df['old_filename'].size
# Broadest directory of old filenames, code will search subfolders
oldfolder = '/Users/sierraflanagan/Documents/filemovertest/'
old_col = 'old_filename' #column heading of old filenames - Changes from .csv to .csv
new_col = 'new_filename' #column heading of new filenames - Changes from .csv to .csv

# Main method searches folders for old filename, and renames ans copies files to new directory
def main():
    for i in range(total_indeces):
        oldName = df.at[i, old_col]
        newName = df.at[i, new_col]
        old_ext = find_filepath(oldName, oldfolder)
        print(oldName)
        new_ext = create_new_filepath(newName)
        shutil.move(old_ext, new_ext)

# Finds filepath given a file name
def find_filepath(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root,name)

# Generates a new filepath to copy and rename files to
def create_new_filepath(newname):
    #The new folder where the renamed files will be moved
    newfolder = '/Users/sierraflanagan/Documents/filemovertest/'
    newfilepath = newfolder + newname
    return newfilepath 

main()
