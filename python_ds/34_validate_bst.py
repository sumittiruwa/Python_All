"""DSA Practice: Validate a Binary Search Tree"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid_bst(node, low=float("-inf"), high=float("inf")):
    if not node:
        return True
    if not (low < node.value < high):
        return False
    return is_valid_bst(node.left, low, node.value) and is_valid_bst(node.right, node.value, high)


if __name__ == "__main__":
    valid_root = TreeNode(5)
    valid_root.left = TreeNode(3)
    valid_root.right = TreeNode(8)
    print("Valid BST:", is_valid_bst(valid_root))

    invalid_root = TreeNode(5)
    invalid_root.left = TreeNode(3)
    invalid_root.right = TreeNode(4)
    print("Invalid BST:", is_valid_bst(invalid_root))
