import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#read csv file
df = pd.read_csv(r'tempYearly.csv')

#set size of graph
sns.set(rc={'figure.figsize' : (12,6)})
#create regession
## sns.scatterplot(x= 'Rainfall', y='Temperature', data=df)

#create regession
sns.regplot(x= 'Rainfall', y='Temperature', data=df)

#show graph in a window
plt.show()

