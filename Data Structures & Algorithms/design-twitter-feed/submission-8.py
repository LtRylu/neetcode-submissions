import heapq

class Twitter:
    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.newsFeed = {}
        self.followers = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (-self.time, tweetId)
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append(tweet)

        if userId not in self.newsFeed:
            self.newsFeed[userId] = []

        heapq.heappush(self.newsFeed[userId], tweet)

        if userId not in self.followers:
            self.followers[userId] = set()

        for user in self.followers[userId]:
            if user not in self.newsFeed:
                self.newsFeed[user] = []
            heapq.heappush(self.newsFeed[user], tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.newsFeed:
            return []

        i = 10
        cur = []
        res = []

        while self.newsFeed[userId] and i > 0:
            tweet = heapq.heappop(self.newsFeed[userId])
            cur.append(tweet)
            res.append(tweet[1])
            i -= 1

        while cur:
            heapq.heappush(self.newsFeed[userId], cur.pop())

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.following:
            self.following[followerId] = set()

        if followeeId in self.following[followerId]:
            return

        self.following[followerId].add(followeeId)

        if followeeId not in self.followers:
            self.followers[followeeId] = set()
        self.followers[followeeId].add(followerId)

        if followerId not in self.newsFeed:
            self.newsFeed[followerId] = []

        for tweet in self.tweets.get(followeeId, []):
            heapq.heappush(self.newsFeed[followerId], tweet)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.following:
            return

        if followeeId not in self.following[followerId]:
            return

        self.following[followerId].remove(followeeId)

        if followeeId in self.followers:
            self.followers[followeeId].remove(followerId)

        if followerId not in self.newsFeed:
            self.newsFeed[followerId] = []

        for tweet in self.tweets.get(followeeId, []):
            if tweet in self.newsFeed[followerId]:
                self.newsFeed[followerId].remove(tweet)

        heapq.heapify(self.newsFeed[followerId])