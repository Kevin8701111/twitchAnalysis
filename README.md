# TwitchAnalysis


## 選題目的
 主要是當初在看實況時 , 實況主表示每天打遊戲 , 打到都對遊戲失去熱情想不到要玩什麼遊戲了, 所以叫觀眾投票 , 投出的結果與觀看人數不成比例 , 原因為4000人進行投票 , 比如票數為 1000,3000,1000 , 遊戲的更換自然會先造成人潮流失 ,再來才會持續增加或減少 , 所以想讓實況主們能夠參考統計數據 , 有效的進行開台時間與人潮的最大效益 。

## 抓取有效資料
 通過twitch 頁面更新抓取由於頁面為渲染畫面 , 通過尋找頁面API進行資料爬取
 2018.04.08-2019.04.08 每天的台灣時間20:00資料進行畫面呈現
 其中官方有幾筆資料為當天伺服器異常 , 故不加以採用
 ![](https://i.imgur.com/jXoO4la.png)
 （圖一）
 明顯的 人數過少, 且許多人討論原因為：國際伺服器異常
 https://www.ptt.cc/bbs/PathofExile/M.1526014583.A.658.html
 


 抓取資料為
 1 . viewers, date, gamename, rownum, day
 2 . starttime, endtime, id

## 遊戲熱度呈現
![](https://i.imgur.com/SRq9MYg.png)
（圖二）
從（圖二）可以觀察到 , 紅色與褐色部份為實況最大宗 , 由於資料為全球的數據所以在亞洲最多人實況與觀看的為League of Legends , 美洲為Fortnite
### 抓取2個主要遊戲進行比較
（圖三）發現2個遊戲的總觀看人數下滑 , 卻還是抱持第一與第二的位子
原來那段期間發生了以下事件：
1 . 國動退出twitch
https://www.4gamers.com.tw/news/detail/34186/cjayride-come-back-and-the-curator-quit-twitch
2 . 館長退出twitch
https://www.ettoday.net/news/20180113/1092199.htm
3 . 金剛直播開播
http://technews.tw/2018/03/01/langlive-2017-performances/

還有一些考試或是節日會導致某個月的觀看人數下滑
![](https://i.imgur.com/fs6nXDU.png)
（圖三）

### 呈現觀眾觀看遊戲類群
圖四呈現前10名遊戲的總人數, 可以看出前三名遙遙領先於其他名次
分別為Fortnite , League of Legends , Grand Theft Auto V
三個的遊戲類別不同分別為
1 .Shooter
2 .MOBA(Multiplayer Online Battle Arena)
3 .Open World
![](https://i.imgur.com/U5EfoWI.png)
（圖四）
![](https://i.imgur.com/FEHH84B.png)
（圖五）
#### 進行觀眾喜愛氣泡圖呈現
由圖得知 , 冷色系 中性色系 暖色系 為主要氣泡圖的階級呈現
對應（圖四）

![](https://i.imgur.com/iwCRPwQ.png)
（圖六）

#### k-Means分群
![](https://i.imgur.com/HKLlI1B.png)
（圖八）
![](https://i.imgur.com/9hWjDkT.png)
（圖八）

```python=
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
```



## 結論
以上數據確實發現某些類群遊戲接連幾年都是排行前三與頻道數成正比 , 之後會加入幾個實況主的開台時間進行時間預測與人數巔峰的數據呈現 , 可以製作成網頁或是APP並且每小時爬取直播平台的數據進行呈現 , 可以讓實況主或是需要的人發現各個遊戲類群的人數多寡 、每日的人潮區間 , 不需要浪費多餘的時間進行實況。










