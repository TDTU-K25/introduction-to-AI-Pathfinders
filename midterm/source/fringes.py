# YC1-2

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def contain(self, u):
        return u in self.items


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

    def push(self, item):
        self.items.append(item)

    def contain(self, u):
        return u in self.items


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, priority, item):
        node = [priority, item]
        if self.is_empty():
            self.items.append(node)
        else:
            for i in range(len(self.items)):
                if node[0] < self.items[i][0]:
                    self.items.insert(i, node)
                    return
            self.items.append(node)

    def remove(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def getPriority(self, item):
        for i in range(len(self.items)):
            if self.items[i][1] == item:
                return self.items[i][0]
        raise ValueError("Item not found in queue")

    def updatePriority(self, item, new_priority):
        for i in range(len(self.items)):
            if self.items[i][1] == item:
                self.items[i][0] = new_priority
                self.items = sorted(self.items, key=lambda x: x[0])
                return
        raise ValueError("Item not found in queue")

    def contain(self, u):
        return u in self.items

    def __str__(self):
        return str(self.items)
