"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            
    def bft(self, starting_vertex):
        que = Queue()
        visited = []
        que.enqueue(starting_vertex)
        while que.size()>0:
            v = que.dequeue()
            if v not in visited:
                visited.append(v)
                for nextnode in self.vertices[v]:
                    que.enqueue(nextnode)
        return visited

    def dft(self, starting_vertex):
        stk = Stack()
        visited = []
        stk.push(starting_vertex)
        while not stk.isEmpty():
            v = stk.pop()
            if v not in visited:
                visited.append(v)
                for nextnode in self.vertices[v]:
                    stk.push(nextnode)
        return visited

    def dft_recursive(self, starting_vertex,visited = None):
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor,visited)

    def bfs(self, starting_vertex, destination_vertex):
        que = Queue()
        visited = []
        que.enqueue([starting_vertex])

        while que.size() > 0:
            path = que.dequeue()
            node = path[-1]

            if node not in visited:
                neighbors = self.vertices[node]
                for neighbor in neighbors:
                    nextPath = list(path)
                    nextPath.append(neighbor)
                    que.enqueue(nextPath)
                    if neighbor == destination_vertex:
                        return nextPath
                visited.append(node)
        return None
                
    def dfs(self, starting_vertex, destination_vertex):
        stk = Stack()
        visited = []
        stk.push([starting_vertex])

        while stk.size() > 0:
            path = stk.pop()
            node = path[-1]

            if node not in visited:
                neighbors = self.vertices[node]
                for neighbor in neighbors:
                    nextPath = list(path)
                    nextPath.append(neighbor)
                    stk.push(nextPath)
                    if neighbor == destination_vertex:
                        return nextPath
                visited.append(node)
        return None









if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
