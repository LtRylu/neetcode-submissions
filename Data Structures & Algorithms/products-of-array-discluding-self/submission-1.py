class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        dictionary = {k: [1, 1] for k in range(len(nums))}
        l = 0
        r = len(nums)-1
        while l < len(nums):
            if l-1 in dictionary:
                dictionary[l][0] = dictionary[l-1][0] * nums[l-1]
            if r+1 in dictionary:
                dictionary[r][1] = dictionary[r+1][1] * nums[r+1]
            l += 1
            r -= 1
        for i in range(len(nums)):
            res.append(dictionary[i][0]*dictionary[i][1])
        return res