from collections import defaultdict

'''
!!!Assumes no cycles!!!

Uses dfs(). Add a node when its children are completely explored.
Complexity:
    Time - O(V + E)
    Space - O(V + E)
            adj - O(V+E)
            visited = O(V)
            _dfs = O(V)
            res = O(V)
'''
class TopologicalSort:
    # graph [[u,v]...]
    def sort(self, graph, N):
        visited = set()
        adj = defaultdict(set)
        # O(E)
        for u, v in graph:
            adj[u].add(v)

        res = []
        # O(V + E)
        for n in range(1, N+1):
            if n in visited:
                continue
            if n not in adj:
                res.append(n)
            else:
                self._dfs(res, n, adj, visited)

        return res[::-1]

    def _dfs(self, res, n, adj, visited):
        visited.add(n)
        # O(E)
        for ad in adj[n]:
            if ad in visited:
                continue
            self._dfs(res, ad, adj, visited)

        res.append(n)


t = TopologicalSort()
#graph = [[1,3], [2,3], [3,4], [4,6], [6,7], [5,6], [2,5], [8,9]]
graph = [[1,4], [2,4], [3,4],[5,1]]
print(t.sort(graph, 5))
