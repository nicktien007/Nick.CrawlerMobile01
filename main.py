import crawlerMobile as Crawler
import ArgumentParserFactory
import fileUtil
import configUtil

config = configUtil.getConfig()
args = ArgumentParserFactory.create(config)
topicName = configUtil.getTopicName(args, config)

print("開始爬取討論區："+ "【" + topicName + "】!!")

sortField = "lastReplyTime" if args.sort == "t" else "replayCount"
topics = Crawler.getTopicsBy(args.code, int(args.page), sortField, bool(args.desc))

print("爬取討論區："+ "【" + topicName + "】" + "共" + str(args.page) + "頁" + "完成!!")

fileName = fileUtil.getFileName(args, config)
fileUtil.saveJson(topics, fileName)

