"""DSA Practice: Binary Tree Height and Diameter"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def diameter(node):
    if not node:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    through_root = left_height + right_height
    return max(through_root, diameter(node.left), diameter(node.right))


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)

    print("Height:", height(root))
    print("Diameter:", diameter(root))
