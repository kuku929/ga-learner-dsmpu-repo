# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here
p_a = len(df[df['fico'] > 700])/len(df)
df1 = df[df['purpose'] == 'debt_consolidation']
p_b = len(df[df['purpose'] == 'debt_consolidation'])/len(df)

df.head()

df2 = df[df['fico'] > 700]
p_a_b = len(df2[df2['purpose'] == 'debt_consolidation'])/len(df2)

p_b_a = p_a_b * p_a / p_b

result = True
if p_b_a == p_a:
    result=True
else:
    result=False

result

prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df)
prob_cs = len(df[df['credit.policy'] == 'Yes'])/len(df)
new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)
bayes = prob_pd_cs * prob_lp/prob_cs

bayes
inst_mean = np.mean(df['installment'])
inst_median = np.median(df['installment'])

plt.hist(df.installment, histtype='stepfilled')
plt.axvline(inst_mean, linestyle='--',color='r')
plt.axvline(inst_median, linestyle='--', color='r')
plt.show()

plt.hist(df['log.annual.inc'])
plt.show()




