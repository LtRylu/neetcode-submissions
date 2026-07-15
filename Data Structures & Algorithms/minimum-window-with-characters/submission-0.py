class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        t_d = {}
        s_d = {}
        l = 0
        res = [len(s) + 1, -1, len(s)]

        for i in range(len(t)):
            t_d[t[i]] = t_d.get(t[i], 0) + 1
        matches = 0
        match_num = len(t_d)

        for r in range(len(s)):
            s_d[s[r]] = s_d.get(s[r], 0) + 1
            if s[r] in t_d and s_d[s[r]] == t_d[s[r]]:
                    matches += 1
            while matches == match_num:
                if r-l < res[0]:
                    res = [r-l, l, r]
                if s[l] in t_d and s_d[s[l]] == t_d[s[l]]:
                    matches -= 1
                s_d[s[l]] -= 1
                l += 1
        if res[0] < len(s) + 1:
            return s[res[1]:res[2]+1]
        return ""
