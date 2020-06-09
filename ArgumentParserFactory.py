from argparse import ArgumentParser

def create(config) :
    description = ""
    for c in config["topicCodes"]:
        description += ':'.join('{}'.format( value) for key, value in c.items()) + "\n"
    
    parser = ArgumentParser(description = ("輸入討論區代碼(code)以進行爬蟲 => " + description + "範例：python3 main.py -c 27 -p 2 -sort r  -desc True"))

    parser.add_argument("-code","-c", help = "討論區代碼(預設值：16，手機板)",dest="code", default="16")
    parser.add_argument("-page","-p", help = "爬取幾頁(預設值：1)",dest="page", default = 1)
    parser.add_argument("-sort","-s", help = "排序欄位 => t:最後回覆時間, r：回應數 (預設值：最後回覆時間)",dest="sort", default = "t")
    parser.add_argument("-desc","-d", help = "降冪排序 => True:由大到小, False：由小到大(預設值：True)",dest="desc", default = True)
    
    return parser.parse_args()