class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        hashMap = {}
        for i in range(n):
            hashMap[i] = []
        for edge1, edge2 in edges:
            hashMap[edge1].append(edge2)
            hashMap[edge2].append(edge1)

        processed = set()
        def dfs(edge, prev):
            if edge in processed:
                return False
            processed.add(edge)
            for i in hashMap[edge]:
                if i != prev:
                    if dfs(i, edge) == False:
                        return False
            return True
        if dfs(0, None) and len(processed) == n:
            return True
        return False
                