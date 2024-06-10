"""Module providing class implementing dijkstra algorithm."""
import heapq
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    """Class implementing dijkstra algorithm"""
    def __init__(self):
        """Initialize an empty graph."""
        self.vertices = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        """Add an edge between two vertices with a specified weight."""
        if from_vertex not in self.vertices:
            self.vertices[from_vertex] = []
        if to_vertex not in self.vertices:
            self.vertices[to_vertex] = []
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))  # Assuming an undirected graph

    def dijkstra(self, start_vertex):
        """
        Compute the shortest paths from a given start vertex to all other vertices using 
        Dijkstra's algorithm.
        """
        # Initialize distances with infinity and set the distance to the start vertex to zero
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0

        # Priority queue to hold vertices to explore
        priority_queue = [(0, start_vertex)]  # (distance, vertex)
        heapq.heapify(priority_queue)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Skip if we found a longer way to current_vertex
            if current_distance > distances[current_vertex]:
                continue

            # Explore neighbors
            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight

                # Only consider this new path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def draw_graph(self):
        """Draw the graph using matplotlib and networkx."""
        G = nx.Graph()

        for vertex, edges in self.vertices.items():
            for edge in edges:
                G.add_edge(vertex, edge[0], weight=edge[1])

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

def main():
    """Main function to create a graph, compute shortest paths, and print the results."""
    # Create a graph
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    # Calculate the shortest paths from vertex 'A'
    start_vertex = 'A'
    distances = g.dijkstra(start_vertex)

    # Print the shortest paths
    print(f"Shortest paths from vertex {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"Distance to {vertex}: {distance}")

    # Draw the graph
    g.draw_graph()

if __name__ == "__main__":
    main()
