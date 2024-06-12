"""Module providing binary tree traversing"""
import heapq
from collections import deque
from task_4 import draw_tree, build_heap_tree

def get_color_gradient(n):
    """Generate a list of colors transitioning from dark to light."""
    colors = []
    for i in range(n):
        intensity = 255 - int(255 * (i / (n - 1)))
        color = f'#{intensity:02X}{intensity:02X}{255:02X}'
        colors.append(color)
    return colors

def dfs_visualization(root):
    """Visualize depth-first search (DFS) traversal of the binary tree."""
    if not root:
        return

    stack = [root]
    order = []
    colors = {}
    node_count = sum(1 for _ in iterate_nodes(root))
    color_gradient = get_color_gradient(node_count)

    colors[root.id] = color_gradient[0]
    draw_tree(root, isDelay=True, window_title="DFS tree visualization")

    while stack:
        node = stack.pop()
        order.append(node)
        if len(order) < node_count:
            colors[node.id] = color_gradient[len(order)]
        else:
            colors[node.id] = color_gradient[-1]

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        draw_tree(root, colors, isDelay=True, window_title="DFS tree visualization")

def bfs_visualization(root):
    """Visualize breadth-first search (BFS) traversal of the binary tree."""
    if not root:
        return

    queue = deque([root])
    order = []
    colors = {}
    node_count = sum(1 for _ in iterate_nodes(root))
    color_gradient = get_color_gradient(node_count)

    colors[root.id] = color_gradient[0]
    draw_tree(root, isDelay=True, window_title="BFS tree visualization")

    while queue:
        node = queue.popleft()
        order.append(node)
        if len(order) < node_count:
            colors[node.id] = color_gradient[len(order)]
        else:
            colors[node.id] = color_gradient[-1]

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        draw_tree(root, colors, isDelay=True, window_title="BFS tree visualization")

def iterate_nodes(root):
    """Generator to iterate over all nodes in the binary tree."""
    if root:
        yield root
        if root.left:
            yield from iterate_nodes(root.left)
        if root.right:
            yield from iterate_nodes(root.right)

def main():
    """
    Main function to create a max-heap, build the corresponding binary tree,
    and visualize DFS and BFS traversals.
    """
    # Create a max-heap using heapq with negated values
    heap = []
    for value in [5, 3, 8, 1, 6, 9, 2]:
        heapq.heappush(heap, -value)  # Negate the value to simulate max-heap

    # Convert negated values back to positive for visualization
    heap = [-x for x in heap]

    # Build the tree from the heap
    root = build_heap_tree(heap)

    # Visualize DFS traversal
    print("Visualizing DFS Traversal:")
    dfs_visualization(root)

    # Visualize BFS traversal
    print("Visualizing BFS Traversal:")
    bfs_visualization(root)

if __name__ == "__main__":
    main()
