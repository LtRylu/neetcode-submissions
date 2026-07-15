class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = set()
        max_count = 0
        sequences.update(nums)
        for num in sequences:
            if num-1 not in sequences:
                count = 1
                while num+1 in sequences:
                    count += 1
                    num += 1
                if count > max_count:
                    max_count = count
        return max_count
                    
                
                

