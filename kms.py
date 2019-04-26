# https://zhuanlan.zhihu.com/p/36499278     線性回歸做時間預測(未達成)

from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

loan_data = pd.DataFrame(pd.read_csv('twitchdatare.csv',header=0))

print(loan_data.head())

loan_data.columns#= Index(['name', 'viewersre', 'rownumre'],dtype='object')

plt.rc('font', family='STXihei', size=10)
plt.scatter(loan_data['viewersre'],loan_data['channelsre'],50,color='blue',marker='+',linewidth=2,alpha=0.8)
plt.xlabel('viewersre')
plt.ylabel('channelsre')
plt.xlim(0,1)
plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='both',alpha=0.4)
# plt.show()

loan = np.array(loan_data[['viewersre','channelsre']])
#取樣

clf=KMeans(n_clusters=3)
#給中心數量
clf=clf.fit(loan)
#進行分群
print( clf.predict([[0.8, 1]]) )
#給順練好的模型一組數據判斷分群
print(clf.cluster_centers_)
#分為3群中心的值


loan_data['label']=clf.labels_
#新增欄位
print(loan_data.head())

loan_data0=loan_data.loc[loan_data["label"] == 0]
loan_data1=loan_data.loc[loan_data["label"] == 1]
loan_data2=loan_data.loc[loan_data["label"] == 2]
#我的欄位label 所被分到的群給予變數

plt.rc('font', family='STXihei', size=10)
#字的樣式
plt.scatter(loan_data0['viewersre'],loan_data0['channelsre'],50,color='#99CC01',marker='+',linewidth=2,alpha=0.8)
#50=點大小 marker = 形式 linewidth = marker寬度 alpha = 透明度
plt.scatter(loan_data1['viewersre'],loan_data1['channelsre'],50,color='#FE0000',marker='*',linewidth=2,alpha=0.8)
plt.scatter(loan_data2['viewersre'],loan_data2['channelsre'],50,color='#0000FE',marker='x',linewidth=2,alpha=0.8)
plt.xlabel('viewersre')
plt.ylabel('channelsre')
plt.xlim(0,1)
# x為0-1
plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='both',alpha=0.4)
# 格線axis= 顯示x或y
plt.show()