class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = [[timestamp, value]]
        else:
            self.keys[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        left = 0
        right = len(self.keys[key]) - 1
        if self.keys[key][left][0] > timestamp:
            return "" 
        while left < right:
            middle = (left + right + 1) // 2
            if self.keys[key][middle][0] > timestamp:
                right = middle - 1
            elif self.keys[key][middle][0] < timestamp:
                left = middle
            else:
                return self.keys[key][middle][1]
        return self.keys[key][left][1]