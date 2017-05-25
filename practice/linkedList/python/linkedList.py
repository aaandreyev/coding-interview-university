class Node:
    def __init__(self, data=None, previous=None, next=None):
        self.data_ = data
        self.next_ = next
        self.previous_ = previous

    def get_data(self):
        return self.data_

    def set_data(self, data):
        self.data_ = data

    def set_next(self, next):
        self.next_ = next

    def get_next(self):
        return self.next_

    def get_previous(self):
        return self.previous_

    def __str__(self):
        return str(self.data_)

class LinkedList(object):


    def __init__(self):
        self.head_ = None
        self.count_ = 0

    def set_head(self, head_node):
        self.head_ = head_node

    # O(n)
    def __len__(self):
        count = 0
        current = self.head_
        while current:
            count += 1
            current = current.get_next()
        return count

    def __str__(self):
        current = self.head_
        output = "START "

        while current:
            output += str(current) + " -> "
            current = current.get_next()

        output += "END"
        return output

    # Pops an item from the front of the list
    # O(1)
    def pop(self):
        if self.head_:
            tmp = self.head_
            self.head_ = self.head_.get_next()
            self.count_ -= 1

            return tmp
        else:
            raise IndexError("Unable to pop from empty list")

    # Returns true if list contains given value
    # O(n)
    def contains(self, value):
        found = False
        current = self.head_
        while current and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()
        return found

    # Deletes all instances of given value in list
    # TODO implement  previous pointers
    def delete(self, value):
        current = self.head_
        prev = None
        while current:
            if current.get_data() == value:
                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.head_ = current.get_next()

                self.count_ -= 1
                break
            else:
                prev = current
                current = current.get_next()

    # Pushes an item to the front of the list
    # O(1)
    def push(self, value):
        node = Node(value)
        node.set_next(self.head_)
        self.set_head(node)
        self.count_ += 1

    # Add an item at the end of the list
    # O(n)
    def append(self, value):
        node = Node(value)
        current = self.head_
        if not current:
            self.head_ = node
            return

        while current.get_next():
            current = current.get_next()

        current.set_next(node)
        self.count_ += 1

    # Checks if empty
    def isEmpty(self):
        return True if self.head_ == None else False

    # Returns a value at the index
    # O(n)
    def valueAt(self, index):
        i = 0
        current = self.head_
        if current == None:
            return current

        while current :
            if index == i:
                return current
            else:
                current = current.get_next()
                i += 1

    #

    # Remove value at the end, and return it
    # O(n)
    def pop_end(self):
        current = self.head_
        prev = None

        if current == None:
            return current

        while current:
            if current.get_next():
                prev = current
                current = current.get_next()
            else:
                if prev != None:
                    prev.set_next(None)

                self.count_ -= 1
                return current


    # Get value at the end
    # O(n)
    def value_end(self):
        return self.valueAt(self.count_ - 1)


    # Insert value at index
    # O(n)
    # Todo implement previous pointer
    def insert(self, index, value):
        node = Node(value)
        ind = 0
        current = self.head_
        prev = None

        if current == None:
            self.head_ = node
            return

        while current and index != ind:
            prev = current
            current = current.get_next()
            ind += 1

        prev.set_next(node)
        node.set_next(current)

    # Empty the whole list
    # O(1)
    def empty(self):
        self.head_ = None
        self.count_ = 0

def main():

    ll = LinkedList()

    print("Initialize, initial size {}".format(len(ll)))
    ll.push(1)
    ll.push(2)
    ll.push(3)

    print("After pushing 1, 2, 3, new size is {}".format(len(ll)))
    print(ll)

    popped = ll.pop()
    print("Popped a value {} from the list".format(popped))
    print(ll)

    ll.push(5)
    ll.push(6)
    ll.push(7)
    ll.push(8)
    print("After pushing 5, 6, 7, 8, new size is {}".format(len(ll)))
    print(ll)

    print("Does list contain 6? : {}".format(ll.contains(6)))

    ll.delete(5)
    print("After deleting value 5, new size is {}".format(len(ll)))
    print(ll)

    ll.append(11)
    ll.append(12)
    ll.append(13)
    print("After appending 11, 12, 13, new size is {}".format(len(ll)))
    print(ll)

    print("Value at the end is {}".format(ll.value_end()))
    print("Value at index 4 is {}".format(ll.valueAt(4)))

    popped1 = ll.pop_end()
    print("Popped value {} at the end, new size is {}".format(popped1, len(ll)))
    print(ll)

    ll.insert(6, 22)
    print("After value 22 is inserted at index 6, new size is {}".format(len(ll)))
    print(ll)

    popped2 = ll.pop_end()
    print("Popped value {} at the end, new size is {}".format(popped2, len(ll)))
    print(ll)


    ll.empty()
    print("After list is emptied, new size is {}".format(len(ll)))
    print("Is lists is empty : ", ll.isEmpty())
    print(ll)

main()