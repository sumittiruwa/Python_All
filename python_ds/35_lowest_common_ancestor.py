"""DSA Practice: Lowest Common Ancestor in a Binary Search Tree"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    current = root
    while current:
        if p < current.value and q < current.value:
            current = current.left
        elif p > current.value and q > current.value:
            current = current.right
        else:
            return current.value
    return None


if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    print("LCA of 2 and 8:", lowest_common_ancestor(root, 2, 8))
    print("LCA of 0 and 4:", lowest_common_ancestor(root, 0, 4))
