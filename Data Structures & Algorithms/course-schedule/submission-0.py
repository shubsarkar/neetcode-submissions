class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's Algorithm - process items in a strict order based on dependencies. 

        # Mental framework, what we need to know is what pre-reqs unlock other questions, as per the graph arrangement

        # prereq : [list of dependent courses]
        # in_deg[X] = 3, this tracks 3 preres we demonstrate using this array

        # start the traversal with the courses that has 0 pre-reqs, push them into queue once processed, remove the dependency from the in_degree array
        # prereq = [[0,1],[1,0]]

        from collections import defaultdict
        from collections import deque

        pre_req = defaultdict(list)
        in_degrees = [0] * numCourses # create in_degrees array, counter for pre-reqs to be defined in the array
        completed_count = 0

        for u, v in prerequisites:
            pre_req[v].append(u)    # 1: 0, 0: 1 and so on
            in_degrees[u] += 1      # [1, 1]
        
        # initialize the queue with courses that has 0 dependencies
        queue = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()

            # as we have taken this course, we subtract 1 from it's indegree and increment the completed_count by 1
            completed_count += 1
            
            for neighbor in pre_req[course]:
                in_degrees[neighbor] -= 1

                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return completed_count == numCourses
            



