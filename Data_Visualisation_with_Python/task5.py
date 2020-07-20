import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# read csv data
data = pd.read_csv(r'./tempYearly.csv')

# print data
print(data)

#plot jointplot graph
sns.jointplot("Rainfall", "Temperature", data=data, kind='reg')

#show graph in a window
#show graph in a window
plt.show()
