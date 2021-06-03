from Preprocessing import preprocessing 
from utility import utility
import os
from utility import utility
import pandas as pd
from model import Energymeter
from model_multi import EnergymeterMulti
import numpy as np
folder_path="tokens"
class_folder=[]
from sklearn import preprocessing
import pickle


low_range=60
high_range=90

#x_test1=np.array([196.011,-28.907,98.131,50.18])
#x_test1=np.array([80.23,2.516,3.33,50.16])
x_test1=np.array([2.181,2.516,3.33,50.16])
modelname="meter.sav"


#x_test1=np.array([202.553,-32.233,205.102,50.2])

def load_data():
    utli_obj=utility()
    print(utli_obj.get_path(folder_path))
    
    #path=utli_obj.get_path(folder_path)
    
    #class_folder=utli_obj.get_file_list(path)
    #print("folder is {} and {}".format(class_folder[0],class_folder[1]))
    data=utli_obj.read_csv()
    
    count=0
    return data
    
def train():
    print ("training start ")
    dataset=load_data()
    meterobject=EnergymeterMulti()
    
    

    
    
    X = dataset.iloc[:,0:4].values
    y = dataset.iloc[:,4].values
    X = np.nan_to_num(X) 
    #dataset_out=np.array(X, int)
    #dataset_out=[int(X) for X in X]
    lab_enc = preprocessing.LabelEncoder()
    X=np.reshape(X,(321*4,1))
    training_scores_encoded = lab_enc.fit_transform(X)
    y = lab_enc.fit_transform(y)
    X=np.reshape(training_scores_encoded,(321,4))
    
    X_tr,x_test,y_tr,t_test=meterobject.train_test_split(X,y)
    #xtrain =[0 if math.isnan(X_tr) else X_tr for X_tr in xtrain]
    #print(xtrain)
    x_train,x_test=meterobject.feature_scaling(X_tr,x_test)
    classifier=meterobject.train_model(x_train,y_tr)
    
    
    
    x_test_r=np.reshape(x_test1,(1,4))

    print("\n \n shape is  is ",x_test_r.shape)

    output=meterobject.prediction(classifier,x_test_r)
    
    print("\n \n output is \n \n",output)
    
    if(output<low_range):
        print("\n \n RUNNING ITEM IS \n")
        print("\n FAN .......")
    elif(output>high_range):
        print("LIST OF RUNNING ITEMS \n \n")

        print("FAN .....MOTOR.....LAPTOP.....IRON")

    pickle.dump(classifier, open(modelname, 'wb'))


    #print('The independent features set: ')
    #print(X[:4,:])
    #print('The dependent variable: ')
    #print(y[:5])
    
    
    
    #print("input is {}".format(label))
    
    
    







if __name__ == "__main__":
    train()
    