"""Module providing functions building tree from heap"""
import heapq
import uuid
from matplotlib import pylab
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    """Class implementing node"""
    def __init__(self, key, color="skyblue"):
        """Initialize a tree node with a given key and color."""
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the node color
        self.id = str(uuid.uuid4())  # Unique identifier for each node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Recursively add edges and nodes to the graph for visualization."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Use id and store node value
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, colors=None, isDelay=False, window_title="Heap tree visualization"):
    """Draw the binary tree using matplotlib and networkx."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors[node[0]] if colors and node[0] in colors \
                   else node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(window_title, figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    if isDelay:
        plt.show(block=False)
        plt.pause(1)
        plt.close()
    else:
        plt.show()


def build_heap_tree(heap):
    """Build a binary tree from a binary heap for visualization."""
    if not heap:
        return None

    nodes = [Node(val) for val in heap]

    for i, node in enumerate(nodes):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):
            node.right = nodes[right_index]

    return nodes[0]  # Root of the heap tree


def main():
    """
    Main function to create a max-heap, build the corresponding binary tree,
    and visualize the tree.
    """
    # Create a max-heap using heapq with negated values
    heap = []
    for value in [5, 3, 8, 1, 6, 9, 2]:
        heapq.heappush(heap, -value)  # Negate the value to simulate max-heap

    # Convert negated values back to positive for visualization
    heap = [-x for x in heap]

    # Build the tree from the heap
    root = build_heap_tree(heap)

    # Draw the heap tree
    draw_tree(root)

if __name__ == "__main__":
    main()