class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}
        unlock = {}

        for i in range(numCourses):
            prereq[i] = set()
            unlock[i] = set()

        for course, pre in prerequisites:
            prereq[course].add(pre)
            unlock[pre].add(course)

        order = []
        processed = set()

        def dfs(cur):
            if cur in processed:
                return

            processed.add(cur)
            order.append(cur)

            for nxt in unlock[cur]:
                if cur in prereq[nxt]:
                    prereq[nxt].remove(cur)

                if not prereq[nxt]:
                    dfs(nxt)

        
        for key in range(numCourses):
            if not prereq[key]:
                dfs(key)

        if len(processed) != numCourses:
            return []
        return order