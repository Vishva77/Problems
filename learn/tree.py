class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_height_balanced(root):
    """Returns True if the given binary tree is height-balanced, False otherwise."""

    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_height_balanced(root.left) and is_height_balanced(root.right)


def height(root):
    """Returns the height of the given binary tree."""

    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1


# Example usage:

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(is_height_balanced(root))  # True
