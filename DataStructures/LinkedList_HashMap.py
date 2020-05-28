import numpy  # Used to create arrays
import doctest


class SinglyLinkedNode(object):

    def __init__(self, item=None, next_link=None, value=None):
        super(SinglyLinkedNode, self).__init__()
        self._item = item
        self._value = value
        self._next = next_link

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    def __repr__(self):
        return repr(self.item)


class SinglyLinkedList(object):
    """
    >>> linkedlist = SinglyLinkedList()
    >>> linkedlist.prepend(2)
    2
    >>> linkedlist.prepend(4)
    4
    >>> linkedlist.prepend(8)
    8
    >>> linkedlist.prepend(23)
    23
    >>> linkedlist.prepend(14)
    14
    >>> linkedlist.display()
    '14 --> 23 --> 8 --> 4 --> 2 '
    >>> linkedlist.remove(2)
    Item  2  is removed from the list
    14
    >>> linkedlist.__contains__(2)
    False
    >>> linkedlist.display()
    '14 --> 23 --> 8 --> 4 '
    """
    def __init__(self, head=None):
        super(SinglyLinkedList, self).__init__()
        self.head = head


    def __len__(self):
        # Returns the length
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count


    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.item
            temp = temp.next


    def __contains__(self, item):
        # Searches for the item
        current = self.head
        if current is None:
            print 'List is empty'
            return False
        found = False
        while current and found is False:
            if current.item == item:
                found = True
            else:
                current = current.next
        if current is None:
            return False
        else:
            return True


    def containskeyvalue(self, key):
        # Search for the key and returns its value
        current = self.head
        found = False
        while current and found is False:
            if current.item == key:
                found = True
            else:
                current = current.next
        if current is None:
            return "Item " + str(key) + " not in the list"
        else:
            return "Key is in the hash table with the value " + current.value


    def remove(self, item):
        # finds item and removes it.
        if self.head is None:
            print 'Empty list'
            return
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.item == item:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            print "Item not in the list"
        if previous is None:           # Deleting first element
            self.head = current.next
        else:
            previous.next = current.next
        print "Item ", item, " is removed from the list"
        return self.head


    def prepend(self, item):
        # adds an item to the front of the list
        new_node = SinglyLinkedNode(item)
        new_node.next = self.head
        self.head = new_node
        return self.head


    def prependKeyValue(self, key, value):
        # adds (key,value) pair to the front of the list
        new_node = SinglyLinkedNode(key)
        new_node._value = value
        new_node.next = self.head
        self.head = new_node
        return self.head


    def __repr__(self):
        s = "List:" + "->".join([item for item in self])
        print s
        return s

    def display(self):
        current = self.head
        if current is None:
            return 'Empty list'
        s = ""
        while current is not None:
            if current.value is not None:
                s += '( '
            s += str(current.item)
            if current.value is not None:
                s += ', ' + current.value + ' )'
            s += " --> "
            current = current.next
        s = s[:-4]  # removing last 4 characters
        return s



class ChainedHashDict(object):
    """
    >>> chainedHashDict = ChainedHashDict()
    >>> chainedHashDict.__setitem__(139, "Sam")
    >>> chainedHashDict.__setitem__(297, "Sri")
    >>> chainedHashDict.display()
    'In Bin 7 - ( 297, Sri ) \\nIn Bin 9 - ( 139, Sam ) \\n'
    >>> chainedHashDict.bin_count
    10
    >>> chainedHashDict.__len__()
    2
    >>> chainedHashDict.__delitem__(297)
    Item  297  is removed from the list
    >>> chainedHashDict.__contains__(297)
    False
    >>> chainedHashDict.__getitem__(139)
    Key is in the hash table with the value Sam
    """
    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(ChainedHashDict, self).__init__()
        self.Table = numpy.empty(bin_count, dtype=object)
        count = 0
        while count < bin_count:
            self.Table[count] = None
            count += 1
        self._max_load = max_load
        self._bin_count = bin_count
        self._hashfunc = hash
        pass

    @property
    def load_factor(self):
        return self._max_load

    @load_factor.setter
    def load_factor(self, max_load):
        self._max_load = max_load
        pass

    @property
    def bin_count(self):
        return self._bin_count

    @bin_count.setter
    def bin_count(self, bin_count):
        self._bin_count = bin_count
        pass

    def rebuild(self, bincount):
        # Rebuilds this hash table with a new bin count
        # Copy current array
        print "Rebuilding table"
        temp = numpy.empty_like(self.Table)
        temp[:] = self.Table
        templength = self.bin_count

        self.bin_count = bincount
        self.Table = numpy.empty(bincount, dtype=object)
        count = 0
        while count != bincount:
            self.Table[count] = None
            count += 1

        count = 0
        while count < templength:
            if temp[count] is not None:
                current = temp[count]
                while current:
                    self.__setitem__(current.item, current.value)
                    current = current.next
            count += 1


    def __getitem__(self, key):
        # Gets the VALUE associated with key
        i = self._hashfunc(key) % self.bin_count
        if self.Table[i] is None:
            print "Key not found"
        linkedlist = SinglyLinkedList()
        linkedlist.head = self.Table[i]
        print linkedlist.containskeyvalue(key)


    def __setitem__(self, key, value):
        # Inserts (key,value) pair
        # Rebuild if load factor is exceeds
        if self.__len__()/float(self.bin_count) >= self.load_factor:
            self.rebuild(2 * self.bin_count)
        linkedlist = SinglyLinkedList()
        i = self._hashfunc(key) % self.bin_count
        if self.Table[i] is None:
            self.Table[i] = linkedlist.prependKeyValue(key, value)
        else:
            linkedlist.head = self.Table[i]
            self.Table[i] = linkedlist.prependKeyValue(key, value)


    def __delitem__(self, key):
        # deletes a node with the given key
        linkedlist = SinglyLinkedList()
        i = self._hashfunc(key) % self.bin_count
        if self.Table[i] is None:
            print "Key ", key, "not present"
        else:
            linkedlist.head = self.Table[i]
            self.Table[i] = linkedlist.remove(key)


    def __contains__(self, key):
        # Searches Key
        linkedlist = SinglyLinkedList()
        i = self._hashfunc(key) % self.bin_count
        if self.Table[i] is None:
            return False
        linkedlist.head = self.Table[i]
        ispresent = linkedlist.__contains__(key)
        return ispresent


    def __len__(self):
        # Computes number of occupied bins
        count = 0
        length = 0
        while count < self.bin_count:
            if self.Table[count] is not None:
                linkedlist = SinglyLinkedList()
                linkedlist.head = self.Table[count]
                length += linkedlist.__len__()
            count += 1
        return length


    def display(self):
        # Returns a string showing the table with multiple lines
        # shows which items are in which bins
        count = 0
        linkedlist = SinglyLinkedList()
        s = ""
        if self.__len__() == 0:
            s = "Table does not have any elements"
            return s
        while count < self.bin_count:
            if self.Table[count] is not None:
                s += "In Bin "
                s += str(count)
                s += " - "
                linkedlist.head = self.Table[count]
                s += linkedlist.display()
                s += "\n"
            count += 1
        return s
        pass


class OpenAddressHashDict(object):
    """
    >>> openaddresshash = OpenAddressHashDict()
    >>> openaddresshash.__setitem__(1, 'open')
    >>> openaddresshash.__setitem__(77, 'hash')
    >>> openaddresshash.display()
    "For index 1 - (1, 'open')\\nFor index 7 - (77, 'hash')\\n"
    >>> openaddresshash.bin_count
    10
    >>> openaddresshash.__len__()
    2
    >>> openaddresshash.__delitem__(77)
    Key 77 deleted
    >>> openaddresshash.__contains__(77)
    False
    >>> openaddresshash.__getitem__(1)
    open
    """
    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(OpenAddressHashDict, self).__init__()

        self.Table = [None]*bin_count
        count = 0
        while count < bin_count:
            self.Table[count] = None
            count += 1
        self._max_load = max_load
        self._bin_count = bin_count
        self._hashfunc = None
        pass

    @property
    def load_factor(self):
        return self._max_load
        pass

    @property
    def bin_count(self):
        return self._bin_count
        pass

    @bin_count.setter
    def bin_count(self, bin_count):
        self._bin_count = bin_count
        pass

    def hash_func(self, key, i):
        return (key + i + 3 * i * i) % self.bin_count
        pass

    def rebuild(self, bincount):
        # Rebuild this hash table with a new bin count
        print 'Rebuilding table'
        temp = numpy.empty_like(self.Table)
        temp[:] = self.Table
        templength = self.bin_count

        self.bin_count = bincount
        self.Table = [None]*bincount
        count = 0
        while count != bincount:
            self.Table[count] = None
            count += 1

        count = 0
        while count < templength:
            if temp[count] is not None:
                    self.__setitem__(temp[count][0], temp[count][1])
            count += 1
        pass

    def __getitem__(self, key):
        # Gets the VALUE associated with key
        count = 0
        while count < self.bin_count:
            i = self.hash_func(key, count)
            if self.Table[i] is not None and self.Table[i][0] == key:
                print self.Table[i][1]
                return
            count += 1
        print 'Key ' + str(key) + ' not found'
        pass

    def __setitem__(self, key, value):
        # Inserts (key,value) pair
        # Rebuild if load factor is exceeds
        if self.__len__()/float(self.bin_count) >= self.load_factor:
            self.rebuild(2 * self.bin_count)

        count = 0
        while count < self.bin_count:
            i = self.hash_func(key, count)
            if self.Table[i] is None or self.Table[i] is 'DELETE':
                self.Table[i] = (key, value)
                break
            count += 1
        pass

    def __delitem__(self, key):
        # Deletes key from the table
        if self.__len__() == 0:
            print 'Table is empty. Cannot delete.'
            return
        count = 0
        while count < self.bin_count:
            i = self.hash_func(key, count)
            if self.Table[i] is not None and self.Table[i][0] == key:
                self.Table[i] = 'DELETE'
                print 'Key ' + str(key) + ' deleted'
                return
            count += 1
        print 'Key ' + str(key) + ' not found'
        pass

    def __contains__(self, key):
        # Searches Key
        if self.__len__() == 0:
            print 'Table is empty'
            return
        count = 0
        while count < self.bin_count:
            i = self.hash_func(key, count)
            if self.Table[i] is not None and self.Table[i][0] == key:
                return True
            count += 1
        return False
        pass

    def __len__(self):
        # Returns length of the table
        count = 0
        len = 0
        while count < self.bin_count:
            if self.Table[count] is not None:
                len += 1
            count += 1
        return len
        pass

    def display(self):
        # Returns a string showing the table with multiple lines
        # showing which items are in which bins
        s = ""
        if self.__len__() == 0:
            s = "Table does not have any elements"
            return s
        count = 0
        while count < self.bin_count:
            if self.Table[count] is not None:
                if self.Table[count] is not 'DELETE':
                    s += "For index "
                    s += str(count)
                    s += " - "
                    s += str(self.Table[count])
                    s += "\n"
            count += 1
        return s
        pass


class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None, parent=None):
        super(BinaryTreeNode, self).__init__()
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTreeDict(object):
    """
    >>> binarytreedict = BinarySearchTreeDict()
    >>> binarytreedict.__setitem__(50, "Kar")
    >>> binarytreedict.__setitem__(23, "AP")
    >>> binarytreedict.__setitem__(87, "Ker")
    >>> binarytreedict.__setitem__(53, "Tam")
    >>> binarytreedict.__setitem__(21, "Mat")
    >>> binarytreedict.__setitem__(17, "Sat")
    >>> binarytreedict.__setitem__(33, "sun")
    >>> binarytreedict.__setitem__(98, "Fun")

    >>> binarytreedict.__delitem__(23)
    Key 23 is deleted from the tree
    >>> binarytreedict.__contains__(23)
    Key  23  is not present in tree
    >>> binarytreedict.__len__()
    7
    >>> binarytreedict.height
    4
    >>> binarytreedict.__getitem__(98)
    Fun
    """
    def __init__(self):
        super(BinarySearchTreeDict, self).__init__()
        self.root = None
        pass

    @property
    def height(self):
        x = self.root
        if x is None:
            return 0
        return self.tree_height(x)
        pass

    def tree_height(self, root):
        x = root
        if x is None:
            return 0
        else:
            return max(self.tree_height(x.left), self.tree_height(x.right)) + 1
        pass

    def _peek(self, stack):
        if len(stack) == 0:
            return None
        else:
            return stack[len(stack)-1]
        pass

    def inorder_keys(self):
        # Using 'yield' and StopIteration exception
        # to return the keys, using an INORDER traversal
        x = self.root
        stack = []
        while x:
            while x.left:
                stack.append(x)
                x = x.left
            yield x.data.key, x.data.value
            while not x.right:
                if stack:
                    x = stack.pop()
                    yield x.data.key, x.data.value
                else:
                    raise StopIteration     # return
            x = x.right
        pass

    def postorder_keys(self):
        # Using 'yield' and 'StopIteration' to yield key in POSTORDER
        x = self.root
        if x is None:
            raise StopIteration  # return
        stack = []
        while True:
            while x:
                if x.right:
                    stack.append(x.right)
                stack.append(x)
                x = x.left
            x = stack.pop()
            if x.right and self._peek(stack) == x.right:
                stack.pop()
                stack.append(x)
                x = x.right
            else:
                yield x.data.key
                x = None
            if len(stack) == 0:
                break
        pass

    def preorder_keys(self):
        # Using 'yield' and 'StopIteration' to yield key in PREORDER
        x = self.root
        if x is None:
            raise StopIteration  # return
        stack = []
        stack.append(x)
        while stack:
            x = stack.pop()
            yield x.data.key
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
        pass

    def items(self):
        # Using 'yield' to return the items (key and value) using
        # an INORDER traversal.
        keys = self.inorder_keys()
        for i in keys:
            yield i
        pass

    def __getitem__(self, key):
        # Gets the VALUE associated with key
        x = self.root
        while x:
            if x.data.key == key:
                print x.data.value
                return
            elif key < x.data.key:
                x = x.left
            else:
                x = x.right
        pass

    def __setitem__(self, key, value):
        # Inserts (key,value) into the tree
        x = self.root
        y = None
        pair = KeyValuePair(key, value)
        z = BinaryTreeNode(pair, None, None, None)
        while x is not None:
            y = x
            if z.data.key < x.data.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.data.key < y.data.key:
            y.left = z
        else:
            y.right = z
        pass

    def tree_min(self, root):
        x = root
        while x.left:
            x = x.left
        return x
        pass

    def tree_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent
        pass

    def __delitem__(self, key):
        # Deletes a tree node
        if self.__len__() == 0:
            print 'Tree is empty'
            return
        x = self.root
        while x:
            if x.data.key == key:
                break
            elif key < x.data.key:
                x = x.left
            else:
                x = x.right
        if x is not None:
            if x.left is None:
                self.tree_transplant(x, x.right)
            elif x.right is None:
                self.tree_transplant(x, x.left)
            else:
                y = self.tree_min(x.right)
                if y.parent != x:
                    self.tree_transplant(y, y.right)
                    y.right = x.right
                    y.right.parent = y
                self.tree_transplant(x, y)
                y.left = x.left
                y.left.parent = y
            print "Key " + str(key) + " is deleted from the tree"
        else:
            print 'Key ' + str(key) + ' not found in the tree'
        pass

    def __contains__(self, key):
        # Searches for the key
        x = self.root
        while x:
            if key == x.data.key:
                print 'Key ', key, 'is present in the tree'
                return
            elif key < x.data.key:
                x = x.left
            else:
                x = x.right
        if x is None:
            print 'Key ', key, ' is not present in tree'
        pass

    def __len__(self):
        # Length of the tree
        keys = self.inorder_keys()
        count = 0
        for i in keys:
            count += 1
        return count
        pass

    def display(self):
        # Prints the keys using INORDER on one
        # line and PREORDER on the next
        print 'Inorder tree traversal'
        keys = self.inorder_keys()
        for i in keys:
            print i[0],
        print '\n'
        print 'Postorder tree traversal'
        keys = self.postorder_keys()
        for i in keys:
            print i,
        print '\n'
        print 'Preorder tree traversal'
        keys = self.preorder_keys()
        for i in keys:
            print i,
        print '\n'
        pass


class KeyValuePair(object):
    def __init__(self, key, value):
        super(KeyValuePair, self).__init__()
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self):
        return repr(self._key) + ":" + repr(self._value)

    pass


def terrible_hash(bin):
    """A terrible hash function that can be used for testing.

    A hash function should produce unpredictable results,
    but it is useful to see what happens to a hash table when
    you use the worst-possible hash function.  The function
    returned from this factory function will always return
    the same number, regardless of the key.

    :param bin:
        The result of the hash function, regardless of which
        item is used.

    :return:
        A python function that can be passes into the constructor
        of a hash table to use for hashing objects.
    """
    def hashfunc(item):
        return bin
    return hashfunc


def main():
    # Thoroughly test your program and produce useful out.
    #
    # Do at least these kinds of tests:
    #  (1)  Check the boundary conditions (empty containers,
    #       full containers, etc)
    #  (2)  Test your hash tables for terrible hash functions
    #       that map to keys in the middle or ends of your
    #       table
    #  (3)  Check your table on 100s or randomly generated
    #       sets of keys to make sure they function
    #
    #  (4)  Make sure that no keys / items are lost, especially
    #       as a result of deleting another key

    # Single Linked List

    print 'Single Linked List'
    print '\n'
    linkedlist = SinglyLinkedList()

    linkedlist.prepend(2)
    linkedlist.prepend(4)
    linkedlist.prepend(8)
    linkedlist.prepend(23)
    linkedlist.prepend(14)

    print 'Contents of the singly linked list are : '
    print linkedlist.display()

    print '\n'

    linkedlist.remove(2)

    print '\n'
    print 'Does list contains 2? '
    print linkedlist.__contains__(2)

    print '\n'

    print 'Contents of the singly linked list are : '
    print linkedlist.display()
    print '\n'
    # Chained Hash Dict
    print 'Chained Hash Dictionary'
    print '\n'
    chainedHashDict = ChainedHashDict()

    chainedHashDict.__setitem__(139, "Sam")
    chainedHashDict.__setitem__(297, "Sri")
    chainedHashDict.__setitem__(309, "ABC")
    chainedHashDict.__setitem__(412, "XYZ")
    chainedHashDict.__setitem__(500, "Blr")
    chainedHashDict.__setitem__(623, "Tmkr")
    chainedHashDict.__setitem__(721, "Mys")

    print 'Contents of the Hash table are : '
    print chainedHashDict.display()

    print '\n'
    print 'Current Bin count is ', chainedHashDict.bin_count

    print '\n'
    print 'Current length of the table is ', chainedHashDict.__len__()

    print '\n'
    print 'Adding four more elements'

    chainedHashDict.__setitem__(888, "Mntr")
    chainedHashDict.__setitem__(102, "Tvkr")
    chainedHashDict.__setitem__(1010, "Agds")
    chainedHashDict.__setitem__(1221, "Cmpa")

    print '\n'
    print 'Bin count increased to ', chainedHashDict.bin_count

    print '\n'
    print 'Contents of the Hash table are : '
    print chainedHashDict.display()

    print '\n'
    print 'Current length of the table is ', chainedHashDict.__len__()

    print '\n'
    chainedHashDict.__delitem__(721)

    print '\n'
    print 'Does hash table contains 721? '
    print chainedHashDict.__contains__(721)

    print '\n'
    print 'Contents of the table after removing 721 are :'
    print chainedHashDict.display()

    print '\n'
    print 'Current length is'
    print chainedHashDict.__len__()

    print '\n'
    print 'Whats the value of the key 1010? '
    chainedHashDict.__getitem__(1010)
    print '\n'
    # OpenAddressHashDict
    print 'OpenAddress Hash Dictionary'
    print '\n'
    openaddresshash = OpenAddressHashDict()

    openaddresshash.__setitem__(1, 'open')
    openaddresshash.__setitem__(999, 'addressing')
    openaddresshash.__setitem__(77, 'hash')
    openaddresshash.__setitem__(82, 'table')
    openaddresshash.__setitem__(90, 'dat')
    openaddresshash.__setitem__(23, 'algo')
    openaddresshash.__setitem__(852, 'blr')

    print 'Contents of the Hash table are : '
    print openaddresshash.display()

    print '\n'
    print 'Current Bin count is ', openaddresshash.bin_count

    print '\n'
    print 'Current length of the table is ', openaddresshash.__len__()

    print '\n'
    print 'Adding four more elements'

    openaddresshash.__setitem__(888, "Mntr")
    openaddresshash.__setitem__(102, "Tvkr")
    openaddresshash.__setitem__(1010, "Agds")
    openaddresshash.__setitem__(1221, "Cmpa")

    print '\n'
    print 'Bin count increased to ', openaddresshash.bin_count

    print '\n'
    print 'Contents of the Hash table are : '
    print openaddresshash.display()

    print '\n'
    print 'Current length of the table is ', openaddresshash.__len__()

    print '\n'
    openaddresshash.__delitem__(888)

    print '\n'
    print 'Does hash table contains 888? '
    print openaddresshash.__contains__(888)

    print '\n'
    print 'Contents of the table after removing 888 are :'
    print openaddresshash.display()

    print '\n'
    print 'Current length is'
    print openaddresshash.__len__()

    print '\n'
    print 'Whats the value of the key 1010? '
    openaddresshash.__getitem__(1010)
    print '\n'
    # BinarySearchTreeDict
    print 'Binary Search Tree Dictionary'
    print '\n'
    binarytreedict = BinarySearchTreeDict()

    binarytreedict.__setitem__(50, "Kar")
    binarytreedict.__setitem__(23, "AP")
    binarytreedict.__setitem__(87, "Ker")
    binarytreedict.__setitem__(53, "Tam")
    binarytreedict.__setitem__(21, "Mat")
    binarytreedict.__setitem__(17, "Sat")
    binarytreedict.__setitem__(33, "sun")
    binarytreedict.__setitem__(98, "Fun")

    binarytreedict.__contains__(23)

    print '\n'
    binarytreedict.__delitem__(23)

    print '\n'
    binarytreedict.__contains__(23)

    print '\n'
    binarytreedict.display()

    print '\n'
    print 'Length of the tree is : '
    print binarytreedict.__len__()

    print '\n'
    print 'Height of the tree : ', binarytreedict.height

    print '\n'
    print 'Whats the value of the key 98? '
    binarytreedict.__getitem__(98)

    pass

if __name__ == '__main__':
    doctest.testmod()
    main()
