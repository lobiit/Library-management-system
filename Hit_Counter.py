class HitCounter(object):

    def __init__(self):
        self.deque = collections.deque()


    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.deque.append(timestamp)



    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        while self.deque and timestamp - self.deque[0] >= 300:
            self.deque.popleft()
        return len(self.deque)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)