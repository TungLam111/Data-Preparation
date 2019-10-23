###Data preparation
file = open('adult.data', 'r')
def chr_int(a) :
	if a.isdigit() :
		return int(a)
	else :
		return 0

data_main = []
for line in file:
	data = line.split(', ')
	if len(data) == 15 :
		data_main.append([chr_int(data[0]), data[1], chr_int(data[2]), data[3], chr_int(data[4]), data[5], data[6], 
			data[7], data[8], data[9], chr_int(data[10]), chr_int(data[11]), chr_int(data[12]), data[13], data[14]])


import pandas as pd 
df = pd.DataFrame(data_main)
df.columns = ['age', 'type_employer', 'fnlwgt', ' education','education_num', 'marital','occupation',
              'relationship','race','sex','capital_gain','capital_loss','hr_per_week','country','income']
##Summarizing the data
counts = df[['country','capital_loss', 'capital_gain']].groupby('country').mean()
high_sal = df[(df['income'] == '>50K\n')]
s1 = df[(df['sex'] == 'Male')]
s2 = df[(df['sex'] == 'Female')]
si1 = df[(df['sex'] == 'Male') & (df['income'] == '>50K\n')]
si2 = df[(df['sex'] == 'Female') & (df['income'] == '>50K\n')]
#ri1 = df[(df['race'] == 'White')& (df['income'] == '>50K\n')]
#ri2 = df[(df['race'] == 'Amer-Indian-Eskimo') & (df['income'] == '>50K\n')]
#ri3 = df[(df['race'] == 'Black') & (df['income'] == '>50K\n')]
#ri4 = df[(df['race'] == 'Other') & (df['income'] == '>50K\n')]
#ri5 = df[(df['race'] == 'Asian-Pac-Islander') & (df['income'] == '>50K\n')]
#print('The average work hours of high income women is ' , si2['hr_per_week'].mean())
#print('The average work hours of high income men is ' , si1['hr_per_week'].mean())
#si11 = si1.groupby('country').size()
#si12 = si1.groupby('country').size()
#print(' The main part of high income men come from ','...',' with ', si11.max())
#print(' The main part of high income women come from ','...',' with ', si12.max())
#print(' The rate of male with income >50K is ', int(len(si1))/int(len(df))*100,'%')
#print(' The rate of female with income >50K is ', int(len(si2))/int(len(df))*100,'%')
#print(' The average of age of women, men is ', df[(df['sex'] == 'Female')].mean(),' ', df[(df['sex']== 'Male')].mean())
#print(' The average of age of high income women, men is ', si1.mean(),' and ',si2.mean())
#print(' The variance of age of high income women, men is ', si1.var(),' and ', si2.var())
#print(' The standard deviation of age of high income women, men is ', si1.std(), ' and ', si2.std())
#print(' The median of age of high income women, men is ', si1.median(), ' and ', si2.median())

# Quantiles and Percentiles
#si1['age'].hist(     normed = 0, histtype = 'stepfilled', alpha =.5, color ='Pink',  bins = 20)
#high_sal['age'].hist(normed = 0, histtype = 'stepfilled', alpha =.5, color ='Red',   bins = 20)
#si1['age'].hist(     normed = 0, histtype = 'stepfilled', alpha =.5, color ='Orange',bins = 20)
#ri1['age'].hist(     normed = 0, histtype = 'stepfilled', alpha =.5, color ='Green', bins = 20)

##Data distribution
#si1['age'].hist( normed = 0, histtype = 'step', alpha =.5 , color = 'Orange', bins = 20)
#si2['age'].hist( normed = 0, histtype = 'step', alpha =.5 , color = 'Blue'  , bins = 20)  #bins = 10 ?!?

##Outlier treatment
#Drop rows which contain missing values and outliers :
#s1_new = s1['age'].drop(s1['age'].index[(s1['age'] > df['age'].median() + 35) & (s1['age'] < df['age'].median() -15)])
#s2_new = s2['age'].drop(s2['age'].index[(s2['age'] > df['age'].median() + 35) & (s2['age'] < df['age'].median() -15)])
#si1_new = si1['age'].drop(si1['age'].index[(si1['age'] > df['age'].median() + 35) & (si1['age'] < df['age'].median() - 15)])
#si2_new = si2['age'].drop(si2['age'].index[(si2['age'] > df['age'].median() + 35) & (si2['age'] < df['age'].median() - 15)])
#print(si1_new.median()," ", si1_new.std())
#print(si2_new.median()," ", si2_new.std())

##Measuring Asymmetry ( độ không cân xứng trong data)
#Skewness

#Pearson

##Sample and estimated mean, Variance and Standard Score
high_sal_age = high_sal['age']
hs_after = high_sal.drop(high_sal_age.index[(high_sal_age > df['age'].median() +35) & (high_sal_age < df['age'].median() -15)])

import numpy as np
err = 0
for i in range (len(hs_after)) :
    x = np.random.normal(hs_after['age'].mean(), hs_after['age'].std() , len(hs_after)) 
    err += ( x.mean() - hs_after['age'].mean())**2 
print("estimated error is " , err/len(hs_after))
