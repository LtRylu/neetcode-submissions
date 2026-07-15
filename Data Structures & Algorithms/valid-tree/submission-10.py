class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        hashMap = {i: [] for i in range(n)}
    
        for a, b in edges:
            hashMap[a].append(b)
            hashMap[b].append(a)

        visited = set()

        def dfs(edge, prev):

            if edge in visited:
                return False

            visited.add(edge)

            for i in hashMap[edge]:
                if i != prev and dfs(i, edge) == False:
                    return False

            return True
        
        return dfs(0, None) and len(visited) == n
                