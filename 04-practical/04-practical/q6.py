# Implement the methods in the Graph class below. Please comment 
# your code as appropriate. It helps us understand your implementation.

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []
        
    def add_node(self, node_value):
        self.nodes.add(node_value)
    
    def add_edge(self, node1, node2):
        # Create an edge between node1 and node2.
        # An edge is just a tuple with two node values in it.
        # Duplicate edges are allowed.
        # for each node in graph
        self.edges.append((node1, node2))
    
    def remove_node(self, node_value):
        # Don't forget to remove edges!
        if node_value in self.nodes:
            self.nodes.remove(node_value)
        if node_value in self.edges[0] or node_value in self.edges[1]:
            #filter the tuple with either value pair is the node to be removed
            self.edges = [item for item in self.edges if item[0] != node_value and item[1] != node_value]
    
    def remove_edge(self, node1, node2):
        # remove one edge between node1 and node2
        edge_remove = (node1, node2)
        if edge_remove in self.edges:
            self.edges.remove(edge_remove)
    
    def get_node(self, node_value):
        # Return a tuple whose first element is the node value
        # and whose second value is a list of edges connected 
        # to the node
        Output = (node_value, list(filter(lambda x:node_value in x, self.edges)))
        return Output
    
def main():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_edge('a', 'c')
    graph.add_edge('b', 'c')
    print(graph.get_node('a'))
    graph.remove_node('b')
    print(graph.get_node('c'))
    
if __name__ == '__main__':
    main()
    
# Expected output:
    
# ('a', [('a', 'c')])
# ('c', [('a', 'c')])  