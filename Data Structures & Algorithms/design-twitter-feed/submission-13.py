import heapq

class Twitter:
    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (-self.time, tweetId)
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId] = set()
        self.following[userId].add(userId)

        res = []
        minHeap = []

        for user in self.following[userId]:
            if user in self.tweets:
                index = len(self.tweets[user]) - 1
                time, tweet = self.tweets[user][index]
                minHeap.append([time, tweet, user, index - 1])
        heapq.heapify(minHeap)

        i = 10
        while minHeap and i > 0:
            time, tweet, user, index = heapq.heappop(minHeap)
            res.append(tweet)
            if index >= 0:
                time, tweet = self.tweets[user][index]
                heapq.heappush(minHeap, [time, tweet, user, index - 1])
            i -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if (followerId == followeeId 
            or followerId not in self.following 
            or followeeId not in self.following[followerId]):
            return

        self.following[followerId].remove(followeeId)