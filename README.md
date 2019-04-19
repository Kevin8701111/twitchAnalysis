# TwitchAnalysis

## 信心擊潰
這次繳交檔案非下禮拜報告的主要內容 , 由於今日報告的人都很棒 , 我認為自己並沒有完整的使用sklearn工具 , 所以再進行一個禮拜的努力

下禮拜預定更新內容:
1 . twitch整天時間數據爬取
2 . 實況主開台數據
3 . 實況主開台時間預測


## 選題目的
 主要是當初在看實況時 , 實況主表示每天打遊戲 , 打到都對遊戲失去樂情想不到要玩什麼遊戲了, 所以叫觀眾投票 , 投出的結果與觀看人數不成比例 , 原因為4000人進行投票 , 比如票數為 1000,3000,1000 , 遊戲的更換自然會先造成人潮流失 ,再來才會持續增加或減少 , 所以想讓實況主們能夠參考統計數據 , 有效的進行開台時間與人潮的最大效益 。

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


## 結論
以上數據可以製作成網頁或是APP並且每小時爬取直播平台的數據進行呈現 , 可以讓實況主或是需要的人發現各個遊戲類群的人數多寡 、每日的人潮區間 , 不需要浪費多餘的時間進行實況。


## 檢討
選擇題目時需要先事先查看資料是否可以拿取完整 , 才不會做到最後時發現資料無法進行有效的預測與正常的資料分群 , 還有事情不能拖到最後幾天才做 , 不然報告的等級會脫離班上平均值。









