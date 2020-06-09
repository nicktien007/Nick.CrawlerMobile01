import urllib.request as req
import bs4
from entity import mobile
from operator import itemgetter, attrgetter

def getHtmlRootBy(url):
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    })
    with req.urlopen(request) as resp:
        data = resp.read().decode("utf-8")

    return bs4.BeautifulSoup(data,"html.parser")

def getTopicUrls(url):
    root = getHtmlRootBy(url)
    titles = root.find_all("div", class_ = "c-listTableTd__title")
    urls = []
    for title in titles:
        if title.a != None:
            urls.append("https://www.mobile01.com/" + title.a["href"])
    return urls

def getTopicUrlsBy(topicCode, page):
    url = "https://www.mobile01.com/forumtopic.php?c=" + str(topicCode)
    urls = []
    currentPage = 1
    while currentPage <= page:
        pageUrl = url + "&p=" + str(currentPage) 
        urls += getTopicUrls(pageUrl)
        currentPage += 1
    return urls

def getReplayUrlsByPage(topicUrl, page):
    urls = []
    currentPage = 2
    while currentPage <= page:
        pageUrl = (topicUrl + "&p=" + str(currentPage))
        urls.append(pageUrl) 
        currentPage += 1
    return urls

def getMaxPageBy(detailRoot):
    paginationRoot = detailRoot.find("ul",class_ = "l-pagination")
    
    if(paginationRoot is None): return 1 #只有一頁

    return paginationRoot.contents[-1].a["data-page"]
    
def getTopicDetailBy(url):
    print(url)
    detailRoot = getHtmlRootBy(url)

    title = detailRoot.find("div",class_ = "l-docking__title").h1.string
    authorId = detailRoot.find("a",class_ = "o-hashtag is-primary").parent.parent.find("a",class_="c-link c-link--gn u-ellipsis")["href"].replace("/userinfo.php?id=","")
    view = detailRoot.find("div",class_="l-navigation__item is-dockingHide").find("ul",class_="l-toolBar").find_all("li")[1].span.string
    createDate = detailRoot.find("div",class_="l-navigation__item is-dockingHide").find("ul",class_="l-toolBar").find_all("li")[0].span.string
    contentStrings = detailRoot.find("div",itemprop="articleBody").stripped_strings
    content = [s for s in contentStrings]
    replays = getReplaysBy(url, detailRoot)

    return mobile.Detail(authorId, title, view, createDate, content, replays)

def getReplaysBy(url, detailRoot):
    replays = getReplaysByPageDetailRoot(detailRoot)

    maxPage = int(getMaxPageBy(detailRoot))
    urls = getReplayUrlsByPage(url, maxPage)
    for url in urls:
        print(url)
        pageDetailRoot = getHtmlRootBy(url)
        replays += getReplaysByPageDetailRoot(pageDetailRoot)
    return replays

def getReplaysByPageDetailRoot(pageDetailRoot):
    replays = []
    articlePages = pageDetailRoot.find_all("div", class_="l-articlePage")
    articlePageLen = len(articlePages)
    count = 1
    while count <= articlePageLen - 1:
        replay = getReplay(articlePages[count])
        replays.append(replay)
        count += 1
    return replays

def getReplay(replayRoot):
    replayUserId = replayRoot.find("div",class_ = "c-authorInfo__id").a["href"].replace("/userinfo.php?id=","")
    replayDate = replayRoot.find("div",class_="l-navigation__item").find("span",class_="o-fNotes o-fSubMini").string
    articleStrings = replayRoot.find("article").stripped_strings
    content = [s for s in articleStrings]
    return mobile.Replay(replayUserId, replayDate, content)

def getTopicsBy(topicCode, page, sortField, isDesc):
    detailUrls = getTopicUrlsBy(topicCode,page)
    details = []
    for url in detailUrls:
        d = getTopicDetailBy(url)
        details.append(d)
    return sorted(details, key = attrgetter(sortField), reverse = isDesc)