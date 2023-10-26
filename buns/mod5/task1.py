class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            return None
        val = self.end
        self.end = self.end.pref
        return val.data

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        val = Node(val)
        if self.end is None:
            self.end = val
        else:
            val.pref = self.end
            self.end = val

    def print(self):
        """
        вывод на печать содержимого стека
        """
        current_node = self.end
        while current_node:
            separator = ' ' if current_node.pref is not None else '\n'
            print(current_node.data, end=separator)
            current_node = current_node.pref
        pass


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.print()

print(stack.pop())
stack.print()