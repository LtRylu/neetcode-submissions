class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        total_woz = 1
        res = []
        count = 0
        for i in nums:
            total *= i
            if i != 0:
                total_woz *= i
            else:
                count += 1
        for i in nums:
            if i == 0:
                if count < 2:
                    res.append(total_woz)
                else:
                    res.append(0)
            else:
                res.append(int(total/i))
        return res