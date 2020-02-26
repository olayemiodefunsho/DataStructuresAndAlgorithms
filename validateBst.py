#O(n) time | O(d) space
def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minVlaue, maxValue):
    if tree is None:
        return True
    if tree.value < minVlaue or tree.value >=  maxValue
        return False
    leftIsValid = validateBstHelper(tree.left, minVlaue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)
