class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}

        for i in range(numCourses):
            prereq[i] = []

        for course, pre in prerequisites:
            prereq[course].append(pre)

        order = []
        processed = set()
        cycle = set()

        def dfs(cur):
            if cur in cycle:
                return False
            if cur in processed:
                return True

            cycle.add(cur)

            for nxt in prereq[cur]:
                if dfs(nxt) == False:
                    return False
            cycle.remove(cur)
            order.append(cur)
            processed.add(cur)

        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return order