class Detail :
    def __init__(self, authorId, title, view, createDate, content ,replayDetail):
        self.authorId = authorId
        self.title = title
        self.view = view
        self.createDate = createDate
        self.content = content
        self.replayDetail = replayDetail
        self.replayCount = len(self.replayDetail) 
        self.lastReplyTime = self.replayDetail[-1].replayDate if (len(replayDetail) > 0) else None
    def __repr__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())

class Replay:
    def __init__(self,replayUserId,replayDate,content):
        self.replayUserId = replayUserId
        self.replayDate = replayDate
        self.content = content
    def __repr__(self):
        return " ".join(self.content)


