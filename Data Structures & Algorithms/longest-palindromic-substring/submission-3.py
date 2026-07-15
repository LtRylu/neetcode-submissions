class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        res = [0, 0]
        def even(p):
            nonlocal length, res
            l = p
            r = p + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > length:
                    res = [l, r]
                    length = r - l
                l -= 1
                r += 1
        def odd(p):
            nonlocal length, res
            l = p - 1
            r = p + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > length:
                    res = [l, r]
                    length = r - l
                l -= 1
                r += 1
        i = 0
        while i < len(s):
            even(i)
            odd(i)
            i += 1
        return s[res[0]:res[1]+1]