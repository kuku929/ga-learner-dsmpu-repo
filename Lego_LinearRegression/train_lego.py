import pandas as pd 
import sklearn
import numpy as np 

lego_train = pd.read_csv(r"C:\Users\Krutarth\Desktop\Datasets\lego_data\train.csv")
lego_train.drop(columns=['Id'], inplace=True)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler_test = StandardScaler()
lego_train['price'] = lego_train['list_price']
lego_train.drop(columns=['list_price'],inplace=True)

lego_train.iloc[:,:-1] = scaler.fit_transform(lego_train.iloc[:,:-1])
lego_train['price'] = scaler_test.fit_transform(np.array(lego_train['price']).reshape(-1,1))
lego_train.to_csv('lego_train.csv')

#print(lego_train.head())

X = lego_train.iloc[:,:-1]
y = lego_train.price

test_lego = pd.read_csv(r'C:\Users\Krutarth\Desktop\Datasets\lego_data\test.csv')
#test.drop(columns=['Id'],inplace=True)
col_name = test_lego.iloc[:,:-1].columns
test = pd.DataFrame(scaler.fit_transform(test_lego.iloc[:,:-1]))
test.columns = col_name



from sklearn.model_selection import train_test_split

#X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.33, random_state=42)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
model = regressor.fit(X,y)
predicted = model.predict(test)

#from sklearn.metrics import r2_score

submission = pd.DataFrame(test_lego.iloc[:,-1])
submission['list_price'] = scaler_test.inverse_transform(predicted)
print(submission.head())

submission.to_csv('submission.csv', index=False)
#print(predicted)