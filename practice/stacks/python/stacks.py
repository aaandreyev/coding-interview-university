class Stack:

    def __init__(self):
        self.items = []
        self.next = None

    def __str__(self):
        output = "START "
        if self.size() > 0:
            for i in iter(self.items):
                output += str(i) + " -> "
            output += " END"
            return output

    def isEmpty(self):
        return self.items == []

    # O(1)
    def push(self, item):
        self.items.append(item)

    # O(1)
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def set_next(self, node):
        next = node

def main():
    st = Stack()

    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    print(st)

    print("Peek: {}".format(st.peek()))
    print(st)

    print("Pop: {}".format(st.pop()))
    print(st)

    print("Stack size is {}".format(st.size()))

    print("Is Stack empty: {}".format(st.isEmpty()))

main()