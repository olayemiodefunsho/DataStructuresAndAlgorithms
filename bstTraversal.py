#O(n) time | O(n) space
def inOrderTreversal(tree, array):
    if tree is not None:
        inOrderTreversal(tree.left, array)
        array.append(tree.value)
        inOrderTreversal(tree.right, array)
    return array


#O(n) time | O(n) space
def preOrderTreversal(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTreversal(tree.left, array)
        preOrderTreversal(tree.right, array)
    return array


#O(n) time | O(n) space
def postOrderTreversal(tree, array):
    if tree is not None:
        postOrderTreversal(tree.left, array)
        postOrderTreversal(tree.right, array)
        array.append(tree.value)
    return array
