class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = {}
        

        for c in tasks:
            freq[c] = 1 + freq.get(c, 0)
        maxVal = max(freq.values())
        nMax = 0
        for key in freq:
            if freq[key] == maxVal:
                nMax += 1
         
        return max(len(tasks), (n+1)*(maxVal-1)+nMax)