import numpy as np
import random
import pandas as pd

def hammingDist(str1, str2): 
    i = 0
    count = 0
  
    while(i < len(str1)): 
        if(str1[i] != str2[i]): 
            count += 1
        i += 1
    return count/len(str1)
    

data_pneumonia_1 = pd.read_csv('cons_pneumonia_1.csv')
data_pneumonia_2 = pd.read_csv('cons_pneumonia_2.csv')
data_pneumonia_3 = pd.read_csv('cons_pneumonia_3.csv')
data_pneumonia_4 = pd.read_csv('cons_pneumonia_4.csv')
data_pneumonia_5 = pd.read_csv('cons_pneumonia_5.csv')

data_normal_1 = pd.read_csv('cons_no_pneumonia_1.csv')
data_normal_2 = pd.read_csv('cons_no_pneumonia_2.csv')
data_normal_3 = pd.read_csv('cons_no_pneumonia_3.csv')
data_normal_4 = pd.read_csv('cons_no_pneumonia_4.csv')
data_normal_5 = pd.read_csv('cons_no_pneumonia_5.csv')

data_pneumonia = [data_pneumonia_1, data_pneumonia_2, data_pneumonia_3, data_pneumonia_4, data_pneumonia_5]
data_normal = [data_normal_1, data_normal_2, data_normal_3, data_normal_4, data_normal_5]

# data preprocessing
data_pneumonia_1 = data_pneumonia_1.drop(['filename'], axis=1)
data_pneumonia_2 = data_pneumonia_2.drop(['filename'], axis=1)
data_pneumonia_3 = data_pneumonia_3.drop(['filename'], axis=1)
data_pneumonia_4 = data_pneumonia_4.drop(['filename'], axis=1)
data_pneumonia_5 = data_pneumonia_5.drop(['filename'], axis=1)


data_normal_1 = data_normal_1.drop(['filename'], axis=1)
data_normal_2 = data_normal_2.drop(['filename'], axis=1)
data_normal_3 = data_normal_3.drop(['filename'], axis=1)
data_normal_4 = data_normal_4.drop(['filename'], axis=1)
data_normal_5 = data_normal_5.drop(['filename'], axis=1)


# hammingDist_pneumonia = []
# hammingDist_normal = []
# hammingDist_between = []

# hammingDist(data_pneumonia[0]['result'].tolist(), data_pneumonia[1]['result'].tolist())

for x in range(0, len(data_pneumonia)):
    for y in range(0, len(data_pneumonia)):
        print(f'Hamming Distance of {x+1} and {y+1} pnemonia: ', round(hammingDist(data_pneumonia[x]['result'].tolist(), data_pneumonia[y]['result'].tolist()), 2))
        print(f'Hamming Distance of {x+1} and {y+1} normal: ', round(hammingDist(data_normal[x]['result'].tolist(), data_normal[y]['result'].tolist()), 2))
        print(f'Hamming Distance of pneumonia {x+1} and normal {y+1}: ', round(hammingDist(data_pneumonia[x]['result'].tolist(), data_normal[y]['result'].tolist()), 2))