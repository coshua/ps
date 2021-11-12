import sys 
from collections import defaultdict
from heapq import *
input = sys.stdin.readline

def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for w, n1, n2 in edges:
        adjacent_edges[n1].append((w, n1, n2))
        adjacent_edges[n2].append((w, n2, n1))
    
    connected_nodes = set()
    connected_nodes.add(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        w, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((w, n1, n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    
    cost = 0
    for w, n1, n2 in mst:
        cost += w
    return cost