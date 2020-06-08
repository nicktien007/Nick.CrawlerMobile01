import json
import codecs
import crawlerMobile as crawler
from operator import itemgetter, attrgetter
from argparse import ArgumentParser
from datetime import datetime


with open("config.json",mode="r") as file:
    config = json.load(file)

description = ""
for c in config["topicCodes"]:
    description += ':'.join('{}'.format( value) for key, value in c.items()) + "\n"

parser = ArgumentParser(description = ("輸入討論區代碼(code)以進行爬蟲 => " + description + "範例：python3 main.py -c 27 -p 2 -sort r  -desc True"))

parser.add_argument("-code","-c", help = "討論區代碼(預設值：16，手機板)",dest="code", default="16")
parser.add_argument("-page","-p", help = "爬取幾頁(預設值：1)",dest="page", default = 1)
parser.add_argument("-sort","-s", help = "排序欄位 => t:最後回覆時間, r：回應數 (預設值：最後回覆時間)",dest="sort", default = "t")
parser.add_argument("-desc","-d", help = "降冪排序 => True:由大到小, False：由小到大(預設值：True)",dest="desc", default = True)
args = parser.parse_args()

now = datetime.now()
dt_string = now.strftime("%Y%m%d%H%M%S")
topicName = list(filter(lambda x: x["topicCode"] == args.code, config["topicCodes"]))[0]["topicName"]
fileName = topicName + "_" + dt_string

print("開始爬取討論區："+ "【" + topicName + "】!!")

topics = crawler.getTopicsBy(args.code,int(args.page))
sortField = "lastReplyTime" if args.sort == "t" else "replayCount"
sortTopics = sorted(topics, key = attrgetter(sortField), reverse = bool(args.desc))

print("爬取討論區："+ "【" + topicName + "】" + "共" + args.page + "頁" + "完成!!")

# print(topics)
# 寫檔(json)
with codecs.open("./output/"+fileName+".json",mode="w" ,encoding = "utf-8") as f:
    json.dump(sortTopics,f, indent = 4, ensure_ascii = False, default = lambda x: x.__dict__)

