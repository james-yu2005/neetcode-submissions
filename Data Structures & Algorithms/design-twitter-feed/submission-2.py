class Twitter:
    def __init__(self):
        self.following = defaultdict(set)
        self.tweet = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)
        news_feed = []
        heap = []

        for Id in self.following[userId]:
            tweet = self.tweet[Id]
            if tweet:
                index = len(tweet)-1
                count, tweet_id = self.tweet[Id][-1]
                heapq.heappush(heap,(count, tweet_id, Id, index-1))
        
        while heap and len(news_feed) < 10:
            count, tweet_id, Id, index = heapq.heappop(heap)
            news_feed.append(tweet_id)
            if index < 0:
                continue
            new_count, new_tweet_id = self.tweet[Id][index]
            heapq.heappush(heap,(new_count, new_tweet_id, Id, index-1))
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


        
