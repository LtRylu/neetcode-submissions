class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        count = 0

        def dfs(root, prev):
            if root in visited:
                return
            visited.add(root)
            for i in adj[root]:
                if i != prev:
                    dfs(i, root)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i, None)
        
        return count