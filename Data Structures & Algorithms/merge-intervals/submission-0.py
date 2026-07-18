class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        i = 0
        while i < len(intervals):
            newInt = [intervals[i][0], intervals[i][1]]
            j = i
            while j < len(intervals) and newInt[1] >= intervals[j][0]:
                newInt[1] = max(newInt[1], intervals[j][1])
                j += 1
            intervals[i:j] = [newInt]
            i += 1
        return intervals