class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxC = 1
        maxFreq = 0
        u = {}

        while r < len(s):
            if s[r] not in u:
                u[s[r]] = 0
            u[s[r]] += 1
            

            maxFreq = max(maxFreq, u[s[r]])

            r += 1

            while r - l - maxFreq > k:  
                u[s[l]] -= 1
                l += 1
            maxC = max(maxC, r - l)

        return maxC