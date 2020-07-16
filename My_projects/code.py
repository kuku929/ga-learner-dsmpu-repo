# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census = np.concatenate((data,new_record), axis=0)
#Code starts here
#np.shape(census)
age = census[:,:1]
#print(age)
max_age = age.max()
min_age = age.min()
age_mean = np.mean(age)
age_std = np.std(age)
#print(max_age, min_age, age_mean, age_std)
race = census[:,2]
race_0 = []
race_1 = []
race_2 = []
race_4 = []
race_3 = []

for i in range(len(census)):
    if race[i] == 0:
        race_0.append(i)
    elif race[i] == 1:
        race_1.append(i)
    elif race[i] == 2:
        race_2.append(i)
    elif race[i] == 3:
        race_3.append(i)
    else:
        race_4.append(i)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

print(len_0, len_1, len_2, len_3, len_4)
minority_race  = 3

senior_citizens = census[:,0] > 60
ser=census[senior_citizens]
#print(np.sum(ser))
senior_citizens_len = len(ser)
working_hours_sum = np.sum(ser[:,6])
#print(working_hours_sum)
#rint(census[:,0])
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

highs = census[:,1] > 10
high = census[highs]
lows = census[:,1] <= 10
low = census[lows]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)
#print(avg_pay_high, avg_pay_low)




