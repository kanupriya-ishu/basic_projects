import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#read csv file
data = pd.read_csv(r'./birthYearly.csv')
#print csv file
print(data)

#create pivoted data
dataP = data.pivot("month", "year", "births")
print(dataP)

#create heatmap
sns.heatmap(dataP, annot=True, fmt="d")

#show graph in a window
plt.show()
