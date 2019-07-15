
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt
data=pd.read_csv('complete_csv.csv')
df=pd.DataFrame(data).fillna(0)
df.rename(columns={'Unnamed: 0':'Year'}, inplace=True)
year=df.iloc[:,0]
gdp_ssa=df.iloc[:,1]
gdp_sk=df.iloc[:,2]
trade_ssa=df.iloc[0:58,3]
trade_sk=df.iloc[0:58,4]
population_ssa=df.iloc[:,5]
population_sk=df.iloc[:,6]
internet_ssa=df.iloc[36:58,7]
internet_sk=df.iloc[36:58,8]
fig, ax = plt.subplots(2, 2)
l1,=ax[0, 0].plot(year,gdp_ssa, 'r') #row=0, col=0
ax[0, 0].plot(year,gdp_sk, 'b') #row=0, col=0
ax[0, 0].set_ylabel('GDP per capita (constant 2010 USD)')
ax[0, 0].set_xlabel('Year')
ax[1, 0].plot(year, population_ssa, 'r')
l,=ax[1, 0].plot(year, population_sk, 'b')
ax[1, 0].set_ylabel('Population')
ax[1, 0].set_xlabel('Year')
ax[0, 1].plot(year[0:58], trade_ssa, 'r')
ax[0, 1].plot(year[0:58], trade_sk, 'b')
ax[0, 1].set_ylabel('Trade (% of GDP)')
ax[0, 1].set_xlabel('Year')
ax[1,1].plot(year[36:58],internet_ssa,'r')
ax[1,1].plot(year[36:58],internet_sk,'b')
ax[1, 1].set_ylabel('Internet (% of population)')
ax[1, 1].set_xlabel('Year')
plt.legend([l,l1],["Republic of Korea", "Sub-Saharan Africa"],loc='best',bbox_to_anchor=(0.5, -0.2),fancybox=False, shadow=False,ncol=3)
plt.show()

