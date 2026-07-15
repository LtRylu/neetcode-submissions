import heapq

class Twitter:
    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.newsFeed = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (-self.time, tweetId)
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        if userId in self.tweets:
            newsFeed.extend(self.tweets[userId])
        if userId in self.following:
            for user in self.following[userId]:
                if user in self.tweets:
                    newsFeed.extend(self.tweets[user])
        heapq.heapify(newsFeed)

        i = 10
        cur = []
        res = []

        while newsFeed and i > 0:
            time, tweet = heapq.heappop(newsFeed)
            res.append(tweet)
            i -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.following:
            self.following[followerId] = set()

        if followeeId in self.following[followerId]:
            return

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.following:
            return

        if followeeId not in self.following[followerId]:
            return

        self.following[followerId].remove(followeeId)