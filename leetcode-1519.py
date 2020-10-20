from collections import defaultdict
from typing import List


class Solution:
    def getSubSize(self, conns, labels, currNode, ans, visited):
        visited.add(currNode)
        if len(conns[currNode]) is 0:
            ans[currNode] = 1
            return {labels[currNode]: 1}
        
        ret = defaultdict(int)
        ret[labels[currNode]] = 1
        for child in conns[currNode]:
            if child not in visited:
                for k, v in self.getSubSize(conns, labels, child, ans, visited).items():
                    ret[k] += v
        
        ans[currNode] = ret[labels[currNode]]
        return ret
    
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [None for x in range(n)]
        conns = defaultdict(list)
        for e in edges:
            f, t = e
            conns[f].append(t)
            conns[t].append(f)
        self.getSubSize(conns, labels, 0, ans, set())
        return ans



n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = 'abaedcd'
s = Solution()
assert s.countSubTrees(n, edges, labels) == [2, 1, 1, 1, 1, 1, 1]

n = 4
edges = [[0,1],[1,2],[0,3]]
labels = 'bbbb'
assert s.countSubTrees(n, edges, labels) == [4, 2, 1, 1]

n = 7
edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]]
labels = 'aaabaaa'
assert s.countSubTrees(n, edges, labels) == [6,5,4,1,3,2,1]


n = 4
edges = [[0,2],[0,3],[1,2]]
labels = 'aeed'
assert s.countSubTrees(n, edges, labels) == [1,1,2,1]