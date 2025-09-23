from collections import defaultdict

def courseScheduleII(numCourses, prereqs):
    graph = defaultdict(list)
    for course, prereq in prereqs:
        graph[prereq].append(course)

    schedule = []
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
        schedule.append(node)
        return True

    
    for i in range(numCourses):
        if not dfs(i):
            return []
        
    return schedule[::-1]
    
print(courseScheduleII(2, [[1, 0]]))
print(courseScheduleII(4, [[1,0],[2,0],[3,1],[3,2]]))