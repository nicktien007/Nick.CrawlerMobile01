# CrawlerMobile01

## Mobile01 討論區代碼

| 代碼  | 討論區 |
| ---- | ------|
| 16   | 手機版 |
| 20   | 相機版 |
| 19   | 筆電版 |
| 17   | 電腦版 |
| 30   | 蘋果版 |
| 28   | 影音版 |
| 21   | 汽車版 |
| 29   | 機車版 |
| 24   | 單車版 |
| 23   | 遊戲版 |
| 26   | 居家版 |
| 27   | 女性版 |
| 31   | 時尚版 |
| 33   | 運動版 |
| 3    | 戶外版 |
| 25   | 生活版 |
| 18   | 旅遊版 |
| 35   | 閒聊版 |
| 36   | 時事版 |


## 相依套件

### 安裝 Beautiful Soup

> https://pypi.org/project/beautifulsoup4/
```python=
# 安裝 Python 3 的 Beautiful Soup 4 模組
pip install beautifulsoup4
```

## 爬蟲調用範例
> 爬取 Mobile01 女性版 1 頁 按照 回應數 進行 降冪排序

```python=
python3 main.py -c 27 -p 2 -sort r -desc True
```


### 參數說明
*   -code CODE, -c CODE  討論區代碼 (**預設值：16，手機板**)
*   -page PAGE, -p PAGE  爬取幾頁 (**預設值：1**)
*   -sort SORT, -s SORT  排序欄位 (**預設值：最後回覆時間**)
    * t：最後回覆時間
    * r：回應數 
*   -desc DESC, -d DESC  降冪排序 (**預設值：True**)
    * True：由大到小進行排序
    * False：由小到大進行排序

## 匯出json檔 說明

> 匯出的Json檔輸出至**output**目錄

- authorId：作者ID
- title：標題
- view：文章人氣
- createDate：時間
- content：內文
- replayDetail：所有回覆
    - replayUserId：回覆者ID
    - replayDate：回覆時間
    - content：回覆內文
- replayCount：回應數
- lastReplyTime：最後回覆時間

### 匯出檔案範例

```json
{
        "authorId": "3075649",
        "title": "(分享)姐姐當家節目-女人想回春 不用靠做夢實現",
        "view": "1749",
        "createDate": "2020-06-03 20:34",
        "content": [
            "最近在看這個節目",
            "這集是在介紹熟齡女性保養",
            "我覺得蠻有重點的",
            "分享給大家",
            "裡面有提到有些很會保養的女藝人(如：余皓然)都是靠吃的保養品",
            "(如鹿胎盤、燕窩、紅蔘等)來保養自己",
            "也有說有一個快50歲的女藝人還生下雙胞胎",
            "保養得很得宜讓人看不出來年紀",
            "真的很羨慕！",
            "不知道各位還有沒有聽過其他女藝人的保養方式？"
        ],
        "replayDetail": [
            {
                "replayUserId": "3286471",
                "replayDate": "2020-06-04 17:25",
                "content": [
                    "瑩明美代子 wrote:",
                    "最近在看這個節目這集(恕刪)",
                    "規律生活是蠻常聽到的",
                    "但現在都市生活很難",
                    "我認識的幾乎都晚睡早起"
                ]
            },
            {
                "replayUserId": "3286544",
                "replayDate": "2020-06-05 18:29",
                "content": [
                    "之前我記得有看過",
                    "鹿胎盤對女生來說是養顏聖品",
                    "女藝人的保養方式百百種",
                    "喝水、蜂蜜水、氣泡水…都有聽過",
                    "還是找到適合自己的比較重要"
                ]
            },
            {
                "replayUserId": "3417464",
                "replayDate": "2020-06-08 17:08",
                "content": [
                    "瑩明美代子 wrote:",
                    "最近在看這個節目這集(恕刪)",
                    "大姊之前有吃過一陣子的鹿胎盤，花一段時間有把身子給調回來，感覺對女生來說還蠻不錯的，身邊沒有實例的話，我還真的不相信保健食品…"
                ]
            },
            {
                "replayUserId": "3075649",
                "replayDate": "2020-06-08 19:10",
                "content": [
                    "sessinge4 wrote:",
                    "之前我記得有看過鹿胎(恕刪)",
                    "真的假的",
                    "我是看到陳明真的新聞才知道有這個東西",
                    "BeckyBecky wrote:",
                    "大姊之前有吃過一陣子...(恕刪)",
                    "大概吃多久啊？她身體怎麼了？"
                ]
            }
        ],
        "replayCount": 4,
        "lastReplyTime": "2020-06-08 19:10"
    }
```