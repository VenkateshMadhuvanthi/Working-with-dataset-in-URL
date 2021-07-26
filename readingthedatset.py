#Header files
import urllib
import urllib.request
import zipfile
import os
import glob
import pandas as pd
'''
Remove # before lines to check the output step by step
You do not have to create any new folder. It will be automatically created under D. Change this path to store the outputs. 
'''
path ="D:/Zoraiz/" #feel free to change it, but change only this.
new_path = path + "zoraiz.zip"
os.makedirs(path) 

#your url
url = 'https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv'
filehandle, _ = urllib.request.urlretrieve(url, new_path )

#create an empty list to store the dataframes
data=[]

#unzipping
with zipfile.ZipFile(new_path,"r") as zip_ref:
    zip_ref.extractall(path + "Output")
    
    
#extracting files
for file in glob.glob(path + "Output/" + '*.csv'): #you can also write this as Output\*.csv
    #just to automate the process like you said.
    print(file) #just to check. Can you see the file names 
    df =pd.read_csv(file, error_bad_lines=False,warn_bad_lines=False) #ignore the formats and the errros
    data.append(df)

#Print the dataset without the NaNs
print(data[0].isna()) #without NAN Values
print(data[1].isna())
print(data[2].isna())

#each data frame refers to csv
#data[0] corresponds to first
#data[1] corresponds to second
#data[2] corresponds to third
