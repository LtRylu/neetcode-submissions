class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ogColor = image[sr][sc]
        visit = set()
        def dfs(r, c, image, visit, color, ogColor):
            if min(r, c) < 0 or r >= len(image) or c >= len(image[0]) or (r,c) in visit or image[r][c] != ogColor:
                return
            else:
                visit.add((r,c))
                image[r][c] = color
                dfs(r+1, c, image, visit, color, ogColor)
                dfs(r-1, c, image, visit, color, ogColor)
                dfs(r, c+1, image, visit, color, ogColor)
                dfs(r, c-1, image, visit, color, ogColor)
        dfs(sr, sc, image, visit, color, ogColor)
        return image