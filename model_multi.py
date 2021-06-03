import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
#from sklearn.externals import joblib

class EnergymeterMulti:
      
    def __init__(self,var="100"):
        self.var=var
        
    def feature_scaling(self,X_train,X_test) :   
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        
        return X_train,X_test
        
    def train_model(self,X_train,y_train):
        classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 42)
        classifier.fit(X_train, y_train)
        return classifier
    
    def save_model(self,classifier):
        print(list(zip(dataset.columns[0:4], classifier.feature_importances_)))
        #joblib.dump(classifier, 'Meterdata.pkl') 
        
        
    def train_test_split(self,X,y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 21)
        
        return X_train,X_test,y_train,y_test
        
    def prediction(self,classifier,x_test):
        y_pred = classifier.predict(x_test)
        return y_pred