import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('data/data.csv')

# df2 = df[df['location'] == 'Chai']
# df3 = df2[df2['measure'] == 'Calcium']

# Crea un dataframe con nuevos valores -> chequear porque dice que usar un dict esta deprecado y sera removido :(
df4 = df.groupby(['location', 'measure']).agg({
    'value': {
        'maxValue': 'max',
        'minValue': 'min',
        'meanValue': 'mean',
        'countValue': 'count'
}})

# df3.plot(x='sample date', y='value')

# plt.show()


