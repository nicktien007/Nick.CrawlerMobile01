from datetime import datetime
import configUtil
import json
import codecs



def getFileName(args, config):
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    topicName = configUtil.getTopicName(args, config)
    return topicName + "_" + dt_string

def saveJson(topics ,fileName):
    with codecs.open("./output/"+ fileName +".json",mode="w" ,encoding = "utf-8") as f:
        json.dump(topics,f, indent = 4, ensure_ascii = False, default = lambda x: x.__dict__)