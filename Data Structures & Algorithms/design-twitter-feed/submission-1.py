class Twitter:

    def __init__(self):
        self.clock = 0 # goes negative, bcoz min heap
        self.tweets = [] # (time, userid, tweetid)
        self.followee = defaultdict(set) # self.followee[userId] give a list of ids user follows
    
    def __createPost(self, uid, tweetid):
        self.clock -= 1
        heapq.heappush(self.tweets, (self.clock, uid, tweetid))

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.__createPost(userId, tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = set(self.followee[userId])
        followees.add(userId)


        copied = self.tweets.copy()
        res = []

        while len(res) < 10 and copied:
            _, uid, tid = heapq.heappop(copied)
            if uid in followees:
                res.append(tid)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followee[followerId]:
            self.followee[followerId].remove(followeeId)
        
