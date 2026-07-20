class Twitter:
    import heapq
    def __init__(self):
        self.users = {}
        self.follows = {}
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.users:
            self.users[userId] = [[tweetId,self.time]]
        else:
            self.users[userId].append([tweetId,self.time])
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for i in self.follows.get(userId,set()):
            if i == userId:
                continue
            for tweet_id, t in self.users.get(i,[]):
                heapq.heappush(heap,(-t,tweet_id))
        for key,val in self.users.get(userId,[]):
            heapq.heappush(heap,(-val,key))
        result = []
        while heap and len(result) < 10:
            result.append(heapq.heappop(heap)[1])
        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)
       
        
