class LinkedNode:
    def __init__(self, value, next_node=None):
        self.val = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = LinkedNode(-1)
        self.tail = self.head
        
    def get(self, index: int) -> int:
        temp = self.head.next
        while temp:
            if index == 0:
                return temp.val
            index -= 1
            temp = temp.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = LinkedNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = LinkedNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        temp = self.head
        while temp and index > 0:
            index -= 1
            temp = temp.next
        
        if temp and temp.next:
            if temp.next == self.tail:
                self.tail = temp
            temp.next = temp.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        temp = self.head.next
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        return arr
