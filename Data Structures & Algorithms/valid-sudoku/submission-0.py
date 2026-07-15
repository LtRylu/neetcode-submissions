class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ### Populate dictionaries
        arr = [
            [[False]*9, [False]*9, [False]*9],
            [[False]*9, [False]*9, [False]*9],
            [[False]*9, [False]*9, [False]*9],
            [[False]*9, [False]*9, [False]*9],
            [[False]*9, [False]*9, [False]*9],
            [[False]*9, [False]*9, [False]*9],
            [[False]*9, [False]*9, [False]*9],
            [[False]*9, [False]*9, [False]*9],
            [[False]*9, [False]*9, [False]*9],
        ]
        for idx, rows in enumerate(board):
            for jdx, nums in enumerate(rows):
                if nums != ".":
                    nums = int(nums)-1 
                    if arr[nums][0][idx]:
                        return False
                    arr[nums][0][idx] = True
                    if arr[nums][1][jdx]:
                        return False
                    arr[nums][1][jdx] = True
                    box_idx = ((jdx) // 3) + ((idx) // 3 * 3)
                    if arr[nums][2][box_idx]:
                        return False
                    arr[nums][2][box_idx] = True
        return True
    


        