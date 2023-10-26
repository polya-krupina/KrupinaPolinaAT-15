class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            return None
        val = self.start
        if self.start == self.end:
            self.start = self.end = None
        else:
            self.start = self.start.nref
            self.start.pref = None
        return val.data

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        val = Node(val)
        if self.start is None:
            self.start = self.end = val
        else:
            val.nref = None
            val.pref = self.end
            self.end.nref = val
            self.end = val

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        val = Node(val)
        if n < 0:
            print('Invalid position')
        elif n == 0:
            val.nref = self.start
            self.start.prev = val
            self.start = val
        else:
            current_node = self.start
            for i in range(n):
                if current_node.nref is None:
                    print('Position is out of bounds')
                    return
                current_node = current_node.nref
            val.nref = current_node
            val.pref = current_node.pref
            current_node.pref.nref = val
            current_node.pref = val


    def print(self):
        """
        вывод на печать содержимого очереди
        """
        current_node = self.start
        while current_node:
            separator = ' ' if current_node.nref is not None else '\n'
            print(current_node.data, end=separator)
            current_node = current_node.nref


queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
queue.print()

print(queue.pop())
queue.print()

queue.insert(2, 6)
queue.print()