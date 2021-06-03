import os
import csv
import pandas as pd
import numpy as np


class utility:
    def __init__(self,init="default"):
        self.init=init
        
    def get_path(self,folder_name):
    
        dir_path=os.path.abspath(folder_name)
        
        return dir_path
    
    
    def get_file_list(self,dir_path):
        file_list=os.listdir(dir_path)
        
        return file_list
    
    def file_open(self,filename):
        file_f = open(filename, "r")
        
        return file_f
        
        
    def read_file(self,filehandle):
        data=filehandle.read()
        return data
    
    def read_line(self,filehandle):
        line_Data=filehandle.readline()
        return line_Data
    
    #def file_write(self,file_name):
    
    def write_csv_file(self,data,label):
        
        with open('MeterData.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Data", "Label"])
            for j in range(len(label)):
                for i in range(len(data)):
                    writer.writerow([data[i],label[j]])
    
    def read_csv(self):
        data=[]
        label=[]
        input_val = pd.read_csv("MeterData_main.csv",usecols=['W','VAR','VA','f','V','PF','A','Label'])
        #new_val=np.isnan(input_val.values.any())

        #data=input_val["Data"]
        #label=input_val['Label']
        return input_val
        
    def data_split(self):
        #Splitting the data into independent and dependent variables
        X = dataset.iloc[:,0:7].values
        y = dataset.iloc[:,7].values
        print('The independent features set: ')
        print(X[:5,:])
        print('The dependent variable: ')
        print(y[:5])