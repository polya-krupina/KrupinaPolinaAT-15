class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None


class LinkedList:
    def __init__(self):
        self.start = None

    def push(self, val):
        node_to_add = Node(val)
        if self.start is None:
            self.start = node_to_add
        else:
            current_node = self.start
            while current_node.nref is not None:
                current_node = current_node.nref
            current_node.nref = node_to_add

    def get(self, index):
        if index < 0:
            return None
        current_node = self.start
        for i in range(index):
            if current_node is None:
                return None
            current_node = current_node.nref
        if current_node is not None:
            return current_node.data
        return None

    def remove(self, index):
        if index == 0:
            if self.start is not None:
                self.start = self.start.nref
        elif index > 0:
            current_node = self.start
            for i in range(index - 1):
                if current_node is None:
                    return
                current_node = current_node.nref
            if current_node is not None and current_node.nref is not None:
                current_node.nref = current_node.nref.nref

    def insert(self, n, val):
        node_to_add = Node(val)
        if n == 0:
            node_to_add.nref = self.start
            self.start = node_to_add
        elif n > 0:
            current_node = self.start
            for i in range(n - 1):
                if current_node is None:
                    return
                current_node = current_node.nref
            if current_node:
                node_to_add.nref = current_node.nref
                current_node.nref = node_to_add

    def __iter__(self):
        current_node = self.start
        while current_node is not None:
            yield current_node.data
            current_node = current_node.nref


linked_list = LinkedList()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)

print(list(linked_list))

print(linked_list.get(1))
print(linked_list.get(3))
print(linked_list.get(-1))

linked_list.remove(1)
print(list(linked_list))

linked_list.insert(1, 2)
print(list(linked_list))
