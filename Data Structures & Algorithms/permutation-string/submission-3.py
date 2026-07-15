class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        
        chars = {}
        s = s2
        for c in s1:
            chars[c] = chars.get(c, 0) + 1
        
        l,r = 0,0
        while r < l2:
            if s[r] not in chars:
                while l <= r:
                    if s[l] in chars:
                        chars[s[l]] += 1
                    l += 1

            elif chars[s[r]] == 0:
                while chars[s[r]] == 0:
                    if s[l] in chars:
                        chars[s[l]] += 1
                    l += 1
            if s[r] in chars:
                chars[s[r]] -= 1
            if r - l + 1== l1:
                return True
            r += 1

        return False