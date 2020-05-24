import heapq
from collections import defaultdict

'''
    The idea is similar to BFS except that we use priority queue to pick next visiting node based on the non-negative weight.
    Time - E log E
    Space - V + E
'''
class Dijkstras:
    def __init__(self):
        self.parent_map = {}  # stores the parent of a node while visiting in the shortest path
        self.dist_map = {}  # stores the distance of a node from source
        self.visited = set()  # tracks visited node
        self.heap_list = []  # acts as min heap

    '''
        graph - [(u,v,w)]   u & v is an edge from u to v with weight w    
    '''
    def find_min_dist(self, source, graph, N):
        # build adj list from graph
        adj = defaultdict(list)
        for (u,v,w) in graph:
            adj[u].append((v, w))

        # initialize distance map
        for n in range(1, N + 1):
            self.dist_map[n] = float("inf")

        # Source initialization
        self.dist_map[source] = 0
        self.parent_map[source] = None

        # Update source distance to 0
        self.heap_list.append((0, source, None))

        while self.heap_list:
            (d, n, p) = heapq.heappop(self.heap_list)

            if n in self.visited:
                continue

            self.visited.add(n)

            self.parent_map[n] = p

            # update the shortest distance of current vertex from source
            self.dist_map[n] = d

            for neighbor, weight in adj[n]:
                if neighbor in self.visited:
                    continue

                dist = self.dist_map[neighbor]
                new_dist = self.dist_map[n] + weight
                if new_dist < dist:
                    #self.parent_map[neighbor] = n
                    heapq.heappush(self.heap_list, (new_dist, neighbor, n))


        print("Shortest path from {0} - ".format(source) + str(self.dist_map))
        print("Parent path - " + str(self.parent_map))


graph = [[2,1,3],[2,3,1],[3,4,1],[2,4,1], [5,6,1], [4,1,1]] # (u,v,w)
d = Dijkstras()
d.find_min_dist(2, graph, 6)














