import pandas as pd 
import matplotlib.pyplot as plt


#create the dataframes using th json file..
df = pd.read_json(r'./rain.json')
print(df)

print("df statistics: ", df.describe())

df.plot(x= 'Month', y = 'Temperature')
df.plot(x= 'Month', y = 'Rainfall')
plt.show()