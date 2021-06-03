import pickle
import numpy as np

#x_test1=np.array([2.181,2.516,3.33,50.16])
modelname="meter.sav"

low_range=60
high_range=90

#x_test1=np.array([202.553,-32.233,205.102,50.2])


#x_test1=np.array([196.011,-28.907,98.131,50.18])
#x_test1=np.array([80.23,2.516,3.33,50.16])
x_test1=np.array([2.181,2.516,3.33,50.16])

def infer():
    loaded_model = pickle.load(open(modelname, 'rb'))
    #result = loaded_model.score(x_test1, Y_test)
    #clf2 = pickle.loads(s)
    x_test_r=np.reshape(x_test1,(1,4))

    output=loaded_model.predict(x_test_r)
    #print(rs)
    
    
    if(output<low_range):
        print("\n \n RUNNING ITEM IS \n")
        print("\n FAN .......")
    elif(output>high_range):
        print("LIST OF RUNNING ITEMS \n \n")

        print("FAN .....MOTOR.....LAPTOP.....IRON")





if __name__ == "__main__":
    infer()