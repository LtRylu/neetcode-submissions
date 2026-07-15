class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        v = -1

        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = v
            v = max(v, temp)
        return arr
