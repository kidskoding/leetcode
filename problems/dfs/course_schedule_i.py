from collections import defaultdict

def courseSchedule(numCourses, prereqs):
    graph = defaultdict(list)
    for course, prereq in prereqs:
        graph[prereq].append(course)

    visited = [0] * numCourses
        
    def dfs(node):
        if visited[node] == 1:
            return False
        if visited[node] == 2:
            return True
        
        visited[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
            
        visited[node] = 2
        return True

    
    for i in range(numCourses):
        if not dfs(i):
            return False
        
    return True
    
print(courseSchedule(2, [[1, 0]]))
print(courseSchedule(2, [[1, 0], [0, 1]]))