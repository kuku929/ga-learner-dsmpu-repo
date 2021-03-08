import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

train = pd.read_csv(r"C:\Users\Krutarth\Desktop\Datasets\greyatom_pricepred\train.csv")
train.drop(columns=['Id'], inplace=True)


#fig, ax = plt.subplots(7,2, figsize=(15,15))

#sns.heatmap(train.corr(),annot=True)
#plt.show()

'''
for i in range(0,X.shape[1]):
    if i <= 6:
        
        ax[i,0].scatter(y=X.iloc[:number,i],x=train.Price[:number])
        ax[i,0].set_title(f"{X.columns[i]} v/s Price")
        
    
    else:

        ax[i-7,1].scatter(y=X.iloc[:number,i],x=train.Price[:number])
        ax[i-7,1].set_title(f"{X.columns[i]} v/s Price")

fig.tight_layout(pad=4)    
plt.show()    
'''
X = train.drop(columns=['Price'])
y = train.Price

from sklearn.preprocessing import PolynomialFeatures
transform_features = PolynomialFeatures(degree=2)
X = pd.DataFrame(transform_features.fit_transform(X))

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X)).drop(columns=[0])

#print(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

lambdas = [0.1,10,1]
lambdas_r = [0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1, 3, 6, 10, 30, 60,70]
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import Ridge
from sklearn.metrics import make_scorer
from sklearn.metrics import r2_score

l2_optimal = Ridge()
grid = GridSearchCV(estimator=l2_optimal, param_grid=dict(alpha=lambdas_r),scoring=make_scorer(r2_score, greater_is_better=True),verbose=3.1)

regressor = grid.fit(X_train,y_train)
print(regressor.best_params_)
y_pred =  regressor.predict(X_test)


score = r2_score(y_test, y_pred)
print(score)
'''
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import make_pipeline

l1_optimal = ElasticNet(alpha=0.125)
l1_optimal = GridSearchCV(estimator=l1_optimal, param_grid=dict(alpha=lambdas))
regressor_l1 = l1_optimal.fit(X,y)
y_pred_l1 = regressor_l1.predict(X_test)
print(regressor_l1.best_params_)
from sklearn.metrics import r2_score
score_l1 = r2_score(y_test, y_pred_l1)
print(score_l1)

'''


