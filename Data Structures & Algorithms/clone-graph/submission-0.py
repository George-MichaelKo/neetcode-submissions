"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # itertae through all nodes elements in the adj list 
            #i am, to first creat ean empty list 
            # i would have a dfs to vist all neighbors and append to list 
        # when i am done exploring all the neigbors of a given node, add the neighbors for that node to the output node
        # i would need a visited set and a output list 

        if not node:
            return None

        seen = dict()

        def dfs(node):
            if node in seen:
                return seen[node]

            clone = Node(node.val)
            seen[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)