import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#create the dataframes using th json file..
df = pd.read_json(r'./rain.json')

plt.figure(figsize=(15,5))
plt.plot(df['Month'], df['Temperature'], label='Termperature')
#plt.show()

#plot rainfall
plt.figure(figsize=(17,5))
plt.plot(df['Month'], df['Rainfall'], label='Rainfall')
#plt.show()

plt.plot(df['Month'], df['Rainfall'], label='Rainfall')
plt.plot(df['Month'], df['Temperature'], label='Termperature')
plt.legend()
plt.show()





















