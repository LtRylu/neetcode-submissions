class LRUCache:
    from collections import deque

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = deque()
        self.qMap = {}
        
        

    def get(self, key: int) -> int:
        if key not in self.qMap:
            return -1
        else:
            self.qMap[key][0] += 1
            self.q.append(key)
            return self.qMap[key][1]

    def put(self, key: int, value: int) -> None:
        if key not in self.qMap:
            self.qMap[key] = [1, value]
        else:
            self.qMap[key][0] += 1
            self.qMap[key][1] = value
        self.q.append(key)
        while len(self.qMap) > self.capacity:
            cur = self.q.popleft()
            self.qMap[cur][0] -= 1
            if self.qMap[cur][0] == 0:
                del self.qMap[cur]
    

        
