
import json

def getTopicName(args, config):
    return list(filter(lambda x: x["topicCode"] == args.code, config["topicCodes"]))[0]["topicName"]

def getConfig():
    with open("config.json", mode="r") as file:
        return json.load(file)