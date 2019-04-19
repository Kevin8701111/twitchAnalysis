# # from sklearn import cluster, datasets, metrics
# # import matplotlib.pyplot as plt
# # import pandas
# # import numpy as np

# df = pandas.read_csv("twitchdata.csv")
# # print(df)
# # # iris = datasets.load_iris()
# # # iris_X = iris.data
# # # silhouette_avgs = []
# # # ks = range(2, 11)
# # # for k in ks:
# # #     kmeans_fit = cluster.KMeans(n_clusters = k).fit(iris_X)
# # #     cluster_labels = kmeans_fit.labels_
# # #     silhouette_avg = metrics.silhouette_score(iris_X, cluster_labels)
# # #     silhouette_avgs.append(silhouette_avg)

# # # plt.bar(ks, silhouette_avgs)
# # # plt.show()
# # # print(silhouette_avgs)
# from sklearn.cluster import KMeans
# from sklearn.externals import joblib
# from sklearn import cluster
# import numpy as np
# import matplotlib.pyplot as plt
 
# data = np.random.rand(100,2)
# print(data)
# estimator=KMeans(n_clusters=3)
# res=estimator.fit_predict(data)
# lable_pred=estimator.labels_
# centroids=estimator.cluster_centers_
# inertia=estimator.inertia_
# #print res
# print(lable_pred)
# print(centroids)
# print(inertia)
 
# for i in range(len(data)):
#     if int(lable_pred[i])==0:
#         plt.scatter(data[i][0],data[i][1],color='red')
#     if int(lable_pred[i])==1:
#         plt.scatter(data[i][0],data[i][1],color='black')
#     if int(lable_pred[i])==2:
#         plt.scatter(data[i][0],data[i][1],color='blue')
# plt.show()





# from sklearn import cluster, datasets
# import pandas
# from sklearn.utils import shuffle

# df = pandas.read_csv("twitchdata.csv")

# df = shuffle(df)
# df = shuffle(df)
# print(df)
# square = df['viewersre'].values
# # square = normalization(square)
# areas = df['rownumre'].values
# # direction = df['direction'].values / 4
# # price = df['price'].values

# iris_X = iris.data

# # kmeans_fit = cluster.KMeans(n_clusters = 3).fit(iris_X)

# # cluster_labels = kmeans_fit.labels_
# # print('ffffffffffffff')
# # print(cluster_labels)
# # print('=========')

# # iris_y = iris.target
# # print('ttttttttttttttt')
# # print(iris_y)


import random
import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv("PeopleNumber.csv")

k = 5
# 先隨機出中心點
centers = []
y = df['viewers'].values
x = df['rownum'].values
centers.append((x, y))

points = []
# 然後在每個中心點的周圍隨機100個點
for x, y in centers:
    for i in range(100):
        px = x + random.random()-0.5
        py = y + random.random()-0.5
        points.append((px, py))

plt.scatter([px for px, py in points], [py for px, py in points], marker='+')
plt.scatter([x for x, y in centers], [y for x, y in centers], marker='o')
plt.show()

# 调用k-means算法，进行聚类分析

# import numpy as np  
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# def DrawBubble(read_name):#气泡图
#     sns.set(style = "whitegrid")#设置样式
#     fp = pd.read_csv(read_name)#数据来源
#     y = fp.rownum#X轴数据
#     x = fp.viewers#Y轴数据
#     z = fp.viewers#用来调整各个点的大小s
#     cm = plt.cm.get_cmap('RdYlBu')
#     fig,ax = plt.subplots(figsize = (12,10))
#     #注意s离散化的方法，因为需要通过点的大小来直观感受其所表示的数值大小
#     #我所使用的是当前点的数值减去集合中的最小值后+0.1再*1000
#     #参数是X轴数据、Y轴数据、各个点的大小、各个点的颜色
#     bubble = ax.scatter(x, y , s = (z - np.min(z) + 0.1) * 1, c = z, cmap = cm, linewidth = 0.5, alpha = 0.5)
#     ax.grid()
#     fig.colorbar(bubble)
#     ax.set_xlabel('viewers', fontsize = 15)#X轴标签
#     ax.set_ylabel('rownum', fontsize = 15)#Y轴标签
#     plt.show()
# if __name__=='__main__':
#     DrawBubble("twitch0418.csv")#气泡图
#     # DrawBubble("PeopleNumber.csv")#气泡图

# from sklearn.cluster import KMeans
# import pandas
# import numpy as np
# import matplotlib.pyplot as plt

# df = pandas.read_csv("twitch0418.csv")

# df_feature = df.iloc[:,1:2]
# # 顯示選取的特徵
# # print(df_feature)
# # ks = range(2, 11)
# # for k in ks:
# # # 使用KMeans分類，K=5
# #     cluster = KMeans(n_clusters=k)
# #     cluster.fit(df_feature)
# #     # 繪製分類的直方圖
# #     plt.xlabel('cluster group')
# #     plt.ylabel('count')
# #     bins = np.arange(0, 10, 0.5) # fixed bin size
# #     plt.hist(cluster.labels_, bins=bins)
# #     plt.show()
# km = KMeans(n_clusters=2)  #K=2群
# y_pred = km.fit_predict(df_feature)
# plt.figure(figsize=(10, 6))
# plt.xlabel('Salary')
# plt.ylabel('Rate of working')
# plt.scatter(df_feature[:,0 ], df_feature[:,1 ], c=y_pred) #C是第三維度 已顏色做維度
# plt.show()