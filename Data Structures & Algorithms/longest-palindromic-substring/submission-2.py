class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        res = [0, 0]
        def even(p):
            l = p
            r = p + 1
            res = [l,l]
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                res =[l, r]
                l -= 1
                r += 1
            return res
        def odd(p):
            l = p - 1
            r = p + 1
            res = [p, p]
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                res = [l, r]
                l -= 1
                r += 1
            return res
        i = 0
        while i < len(s):
            l, r = even(i)
            if r - l > length:
                res = [l, r]
                length = r - l
            l, r = odd(i)
            if r - l > length:
                res = [l, r]
                length = r - l
            i += 1
        return s[res[0]:res[1]+1]