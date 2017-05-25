class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        output = "START "

        for i in iter(self.items):
            output += str(i) + " -> "
        output += " END"
        return output

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if self.items != []:
            return self.items[0]
        return -1

    def add(self, data):
        self.items.insert(0, data)

    def remove(self):
        return self.items.pop()

def main():
    q = Queue()

    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    print(q)

    q.remove()
    print(q)

    q.add(5)
    q.add(6)
    print(q)

    q.remove()
    q.remove()
    print(q)
main()