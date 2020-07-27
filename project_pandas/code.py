# --------------
import pandas as pd
import numpy as np


bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include='object')
print('categorical shape',categorical_var.shape)
numerical_var = bank.select_dtypes(include = 'number')
print('numerical shape', numerical_var.shape)

banks = bank.drop('Loan_ID', axis=1)
bank_mode = banks.mode()
bank_mode.iloc[0,0]
x = 0
for col in banks.columns:
    banks[col].fillna(bank_mode.iloc[0,x], inplace=True)
    x += 1
avg_loan_amount = pd.pivot_table(data=banks, index=['Married', 'Self_Employed','Gender'], values='LoanAmount', aggfunc='mean')


loan_approved_s = banks[banks['Self_Employed'] == 'Yes']
loan_approved_se = loan_approved_s[loan_approved_s['Loan_Status'] == 'Y']

loan_approved_su = banks[banks['Self_Employed'] == 'No']
loan_approved_nse = loan_approved_su[loan_approved_su['Loan_Status'] == 'Y']
percentage_se = loan_approved_se.shape[0]/614 * 100
percentage_nse = loan_approved_nse.shape[0]/614 * 100
print(percentage_nse, percentage_se)

banks['Loan_Amount_Term'] = banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term= banks[banks['Loan_Amount_Term'] >= 25].shape[0]
print(big_loan_term)

loan_groupby = banks.groupby('Loan_Status').mean()
mean_values = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values.iloc[1,0]



