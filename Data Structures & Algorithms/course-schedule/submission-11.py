class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for course,pre in prerequisites:
            prereqs[course].append(pre)
        print(prereqs)
        visited = set()
        seen = set()
        def cycle_det(course,seen):
            if course in seen:
                return True
            if course in visited:
                return False
            seen.add(course)
            for crs in prereqs[course]:
                if cycle_det(crs,seen):
                    return True
            seen.remove(course)
            visited.add(course)
            return False

        # if there is a cycle, then its impossible?
        for i in range(numCourses):
            if i not in visited:
                if cycle_det(i,set()):
                    return False
        return True

        

