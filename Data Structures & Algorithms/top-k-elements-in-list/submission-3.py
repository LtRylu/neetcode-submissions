class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        len_list = len(nums)
        k_list = {}
        k_lowest = 1
        count = {}
        occurrences = {}
        i = 0
        while len(count) < k:
            if nums[i] not in count:
                count[nums[i]] = 1
                k_list[nums[i]] = 1
                occurrences.setdefault(1, []).append(nums[i])
            else:
                occurrences[count[nums[i]]].remove(nums[i])
                count[nums[i]] += 1
                k_list[nums[i]] += 1
                occurrences.setdefault(count[nums[i]], []).append(nums[i])
            i += 1

        while i < len_list:
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
                if nums[i] not in k_list and count[nums[i]] > k_lowest:
                    k_list[nums[i]] = count[nums[i]]
                    occurrences.setdefault(count[nums[i]], []).append(nums[i])
                    
                    del k_list[occurrences[k_lowest].pop()]
                elif nums[i] in k_list:
                    occurrences[count[nums[i]]-1].remove(nums[i])
                    occurrences.setdefault(count[nums[i]], []).append(nums[i])
                if not occurrences[k_lowest]:
                        k_lowest +=1
            i += 1
        return list(k_list.keys())

