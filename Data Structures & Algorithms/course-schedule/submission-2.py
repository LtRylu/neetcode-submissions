class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        unlock = {}

        for i in prerequisites:
            if i[1] not in prereq:
                prereq[i[1]] = set()
            if i[0] not in prereq:
                prereq[i[0]] = set()

            prereq[i[0]].add(i[1])

            if i[1] not in unlock:
                unlock[i[1]] = set()
            if i[0] not in unlock:
                unlock[i[0]] = set()

            unlock[i[1]].add(i[0])

        def dfs(cur):
            for i in unlock[cur]:
                if cur in prereq[i]:
                    prereq[i].remove(cur)
                if not prereq[i]:
                    dfs(i)

        for key in list(prereq.keys()):
            if not prereq[key]:
                dfs(key)

        for key in prereq.keys():
            if prereq[key]:
                return False

        return True