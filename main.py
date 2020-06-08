import json
import codecs
import crawlerMobile as crawler

topics = crawler.getTopicsBy(27,1)
# print(topics)
# 寫檔(json)
with codecs.open("./output/j.json",mode="w" ,encoding = "utf-8") as f:
    # j = json.dumps(topics, default=lambda x: x.__dict__ ,indent=4, ensure_ascii=False)
    json.dump(topics,f, indent = 4, ensure_ascii = False, default = lambda x: x.__dict__)

