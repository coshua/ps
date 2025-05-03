class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        def coloring(graph, colors, id, cur):
            if colors[id] != 0:
                return colors[id] == cur
            
            colors[id] = cur

            for i in graph[id]:
                if not coloring(graph, colors, i, -cur):
                    return False
            
            return True
                
        colors = [0] * len(graph)

        for i in range(len(graph)):
            if colors[i] == 0 and not coloring(graph, colors, i, 1):
                return False
        
        return True