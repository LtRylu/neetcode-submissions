class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        l,r = 0,0
        chars = {}
        s = s2

        if l1 > l2:
            return False
        
        for c in s1:
            chars[c] = chars.get(c, 0) + 1
        
        while r < l2:
            while (s[r] not in chars and l <= r) or (s[r] in chars and chars[s[r]] == 0):
                if s[l] in chars:
                    chars[s[l]] += 1
                l += 1
            if s[r] in chars:
                chars[s[r]] -= 1
            if r - l + 1 == l1:
                return True
            r += 1

        return False