import pandas as pd
import seaborn
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import metrics


data_pneumonia = pd.read_csv('train_pneumonia.csv')
data_normal = pd.read_csv('train_no_pneumonia.csv')

data_pneumonia = data_pneumonia.assign(truth = np.ones(len(data_pneumonia['filename'])))
data_normal = data_normal.assign(truth = np.zeros(len(data_normal['filename'])))

data_list = [data_pneumonia, data_normal]

data = pd.concat(data_list, ignore_index=True)

data['result'].replace(['B','A'], [0,1], inplace=True)
data = data.drop(['filename'], axis=1)
data = data.fillna(0)

confusion_matrix = metrics.confusion_matrix(data['truth'], data['result'])
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])

F1 = metrics.f1_score(data['truth'],data['result'], average='macro')
recall = metrics.recall_score(data['truth'],data['result'], average='macro')
precision = metrics.precision_score(data['truth'],data['result'], average='macro')
accuracy = metrics.accuracy_score(data['truth'],data['result'])

print("Accuracy: ", accuracy)
print("F1: ", F1)
print("Recall: ", recall)
print("Precision: ", precision)

cm_display.plot()
plt.show()

