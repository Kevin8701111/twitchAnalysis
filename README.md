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

# Twitch - 關聯

## 選題目的
由於期中是做 人數和類群分析 , 本來是想做實況主的開台時間預測 , 但很難做不出來 , 所以選擇使用apriori 做觀眾對 實況主 的關聯性

## 資料來源
Twitch api:
https://dev.twitch.tv/docs/api/reference/#get-extension-analytics

官方提供的API 主要抓取==遊戲類群== 觀看總人數 ==前10名== , ==類群==裡前==100位實況主== , ==實況主==聊天室內==所有觀眾==

![](https://i.imgur.com/EVPUyF4.png)
因為資料量很大 , 電腦load檔案就會有memory err的問題 , 所以切成==一個星期10個group==

## 遇到的狀況
1. load檔案的時候Memory err
![](https://i.imgur.com/KBX8jot.png)
2. Data 型態不同
![](https://i.imgur.com/LnvN32M.png)
3. Dataframe is to big
在借用學長的電腦跑得時候出現的 , ram32G

## 實做步驟
1.
目的：解決資料一次讀進來時 , 記憶體不足
```python=
df1 = pd.read_csv('./10_grand_theft_auto_v/twitch_0601_0607.txt', sep=",", chunksize = 100000, header=None, names=["mid", "viewer", "group", "master"])
# # print(df1)
df2 = pd.read_csv('./10_grand_theft_auto_v/twitch_0608_0614.txt', sep=",", chunksize = 100000, header=None, names=["mid", "viewer", "group", "master"])
# print(df2)
df = pd.DataFrame(columns=[]) 
```
2. 
合併使用chunksize ,生成的迭代器 並重新給index
```python=
for df1 in df1:
#     print(df1)
#     print(type(df1))
    df3 = pd.concat([df,df1],ignore_index=True)
for df2 in df2: 
#     print(df2)
#     print(type(df2))
    df4 = pd.concat([df,df2],ignore_index=True) 
```
3. 
2個星期合併
```python=
res = pd.concat([df3, df4],  axis=0)
res['count'] = 1
```
4. 
```python=
new = res.pivot_table(index = 'viewer', columns = 'master', values = 'count', fill_value = 0, aggfunc = np.sum)

```
5. 
```python=
def encode_units(x):
    if x <= 0:
        return 0
    if x>= 1:
        return 1

new_sets = new.applymap(encode_units)
print(type(new_sets))

```
6.
```python=
frequent_itemsets = apriori(new_sets, min_support = 0.01, use_colnames = True)
```
7.
```python=
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold = 0.1)
```
## 解釋結果
![](https://i.imgur.com/59RohPC.png)

#### 找尋可以解釋的關聯性
1 . overpow - LOL
![](https://i.imgur.com/cEJecf8.png)

2 . buli - GTA5
![](https://i.imgur.com/yhe9GJ0.png)

##### 這時候我才想到我使用的資料是2018/06月的

到這個網站找歷史資料
1. https://sullygnome.com/channel/overpow/2018june/streams
2. https://sullygnome.com/channel/buli/2018june/streams

最後覺得有點不知如何是好 , 只好直接google ==Overpow Buli bonkol twitch==

找到了這個!!
https://www.youtube.com/watch?reload=9&v=LRap6v6ETU8&list=PLMsFl8i4WNRcmYAXrdkv3O4RJedYvDLzY&index=4&fbclid=IwAR0JYVnknp5SYIUg1nM8PTfh0Pm9gEA4fGxn5gEMQk-zAWzjbbN3a-KHAC0

所以在我使用的資料裡面 , 可以發現觀眾看的實況主們==Overpow== ==Buli== ==bonkol== 是比較多人同時或都會觀看的
![](https://i.imgur.com/kmTRoiJ.png)

## 結論
在觀看youtube剪輯的時候發現這幾位實況主原來 在6月份的時候是一起玩遊戲的 , 所以觀眾在看其中一個實況主的時候 , 也會好奇另一個在同一個伺服器裡的實況主在做什麼, 所以才會出現這3位實況主有那麼強的關聯性








