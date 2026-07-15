class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = i
            else:
                return True
        return False