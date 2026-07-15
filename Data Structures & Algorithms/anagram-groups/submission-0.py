class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        out = []
        count = 0
        for word in strs:
            Sword = ''.join(sorted(word))
            if Sword not in ana:
                ana[Sword] = [word, count]
                count += 1
                out.append([word])
            else:
                out[ana[Sword][1]].append(word)
        
        return out
        