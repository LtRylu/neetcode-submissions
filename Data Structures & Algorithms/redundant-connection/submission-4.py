class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}

        for n1, n2 in edges:
            if n1 not in par:
                par[n1] = n1
                rank[n1] = 1
            if n2 not in par:
                par[n2] = n2
                rank[n2] = 1

        def find(a):
            res = a
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 1
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 0
        valid = []
        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]
        return valid[-1]