class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        i = 0
        merged = []
        while i < len(intervals):
            newInt = [intervals[i][0], intervals[i][1]]
            j = i
            while j < len(intervals) and newInt[1] >= intervals[j][0]:
                newInt[1] = max(newInt[1], intervals[j][1])
                j += 1
            merged.append(newInt)
            i = j
        return merged