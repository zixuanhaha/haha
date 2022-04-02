##二项式分布

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats

import pandas as pd
import seaborn as sns

n = 20
p = 0.3
k = np.arange(0, 41)
# 定义二项分布
binomial = stats.binom.pmf(k, n, p)

# 二项分布可视化
plt.plot(k, binomial, 'o-')
plt.title('binomial:n=%i,p=%.2f' % (n, p), fontsize=15)
plt.xlabel('number of success')
plt.ylabel('probability of success', fontsize=15)
plt.grid(True)
plt.show()

# 探索特征分布、相关性
data1=pd.read_csv('/Volumes/学习/git/haha/hour.csv',header=0)
#data_pd=data1.toPandas()
sns.set(style='whitegrid',context='notebook')
cols=['temp','atemp','label']
sns.pairplot(data1[cols],height=2.5)
plt.show()