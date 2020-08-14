# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)
data.columns
#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()

#Plotting bar plot
figure = plt.figure(figsize=(7,10))
plt.bar(loan_status.index, loan_status)
loan_status[1]
# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(10,18))


#Changing the x-axis label
plt.xlabel('Property Area')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)
plt.show()
property_and_loan['Y'][0]
# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=True, figsize=(10,10))

#Changing the x-axis label
plt.xlabel('Education Status')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)
plt.show()
# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data["Education"] == 'Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate = data[data["Education"] == 'Not Graduate']

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density', label='Graduate')

#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')
plt.show()
#For automatic legend display


# Step 5
#Setting up the subplots
fig, (ax1,ax2,ax3) = plt.subplots(3,1,figsize=(10,10))

#Plotting scatter plot
data.plot.scatter(x='ApplicantIncome', y='LoanAmount', ax=ax1)

#Setting the subplot axis title
plt.title('Applicant Income')

#Plotting scatter plot
data.plot.scatter(x='CoapplicantIncome', y='LoanAmount', ax=ax2)

#Setting the subplot axis title
plt.title('Coapplicant Income')

#Creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome']  + data['CoapplicantIncome']

#Plotting scatter plot
data.plot.scatter(x='TotalIncome', y = 'LoanAmount', ax=ax3)


#Setting the subplot axis title
plt.title('Total Income')



