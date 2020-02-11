class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        pass

    def setTail(self, node):
        pass

    def insertBefore(self, node, nodeToInsert):
        pass

    def insertAfter(self, node, nodeToInsert):
        pass

    def insertAtPosition(self, node, nodeToInsert):
        pass

    def removeNodesWithValue(self, node):
        pass

    def remove(self, node):
        pass

    def containsNodesWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None