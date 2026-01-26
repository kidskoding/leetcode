from collections import defaultdict

def find_order(tasks, deps):
    graph = defaultdict(list)
    for x in deps:
        graph[x[0]].append(x[1])
    
    def dfs(node):
        pass
        
    print(graph)
    
print(find_order(["A", "B", "C", "D"], [["A","B"], ["B","C"], ["A","D"]]))
