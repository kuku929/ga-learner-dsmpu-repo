# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
data['Gender'].replace({
    '-':'Agender'
}, inplace=True)
data.Gender.unique()

data['Gender'].value_counts().plot(kind='bar')
plt.show()

data.Alignment.value_counts().plot(kind='bar')
plt.ylabel('count')
plt.xlabel('type')
plt.show()

covi = data.cov().iloc[1,6]
covs = data.cov().iloc[2,6]
stdc=data['Combat'].std()
stdi=data['Intelligence'].std()
stds=data['Strength'].std()
pei = covi/stdi/stdc
pes = covs/stds/stdc
data.corr(method='pearson')

data['Total'].quantile(q=0.99)

super_best_names = data[data['Total'] > data['Total'].quantile(0.99)]['Name']
super_best_names = np.array(super_best_names)
# Code starts here



