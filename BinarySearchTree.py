from TreeNode import TreeNode

# Author: Jake Writer
# purpose: This program creates a BinarySearchTree and its required methods
# Date: 12/8/19
class BinarySearchTree:
    # name: Constructor
    # assumptions: none
    # input: nothing (self)
    # output: none
    def __init__(self):
        self.root = None

    # name: size
    # assumptions: it exists
    # input: nothing (self)
    # output: the size of the dictionary
    def size(self):
        if self.root is None:
            return 0
        return self.root.getSize()

    # recursive element of size()
    def nsize(self, n):
        sum = 1
        if n.getLeft() is not None:
            sum += n.getLeft().getSize()
        if n.getRight() is not None:
            sum += n.getRight().getSize()
        return sum

    # name: isEmpty
    # assumptions: exists
    # input: none
    # output: boolean
    def isEmpty(self):
        if self.size() is 0:
            return True
        else:
            return False

    # name: put
    # assumptions: it exists
    # input: key and value
    # output: no output, but adds an element to the BinarySearchTree
    def put(self, key, value):
        self.root = self.rput(self.root, key, value)

    # recursive element of put
    def rput(self, n, key, value):
        if n is None:
            n = TreeNode(key, value, 1)
            return n
        if n.getKey() > key:
            if n.getLeft() is None:
                newNode = TreeNode(key, value, 1)
                n.setLeft(newNode)
            else:
                n.setLeft(self.rput(n.getLeft(), key, value))
        if n.getKey() < key:
            if n.getRight() is None:
                newNode = TreeNode(key, value, 1)
                n.setRight(newNode)
            else:
                n.setRight(self.rput(n.getRight(), key, value))
        if n.getKey() is key:
            n.setValue(value)

        n.setSize(self.nsize(n))
        return n

    # name: get
    # assumptions: exists
    # input: key
    # output: None or the value at the key
    def get(self, key):
        return self.rget(self.root, key);

    # recursive element of get
    def rget(self, n, key):
        if n is None:
            return None
        if n.getKey() > key:

            if n.getLeft() is None:
                return None
            else:
                return self.rget(n.getLeft(), key)
        if n.getKey() < key:
            if n.getRight() is None:
                return None
            else:
                return self.rget(n.getRight(), key)
        if n.getKey() == key:
            return n.getValue()

    # name: contains
    # assumptions: exists
    # input: key
    # output: true if the dictionary contains the key, else false
    def contains(self, key):
        if self.get(key) is not None:
            return True
        else:
            return False

    # name: remove
    # assumptions: exists
    # input: key
    # output: error or the value of the removed key
    def remove(self, key):
        v = self.get(key)
        self.root = self.rremove(self.root, key)
        return v

    # recursive element of remove
    def rremove(self, n, key):
        if n is None:
            return None
        else:
            if n.getKey() > key:
                n.setLeft(self.rremove(n.getLeft(), key))
            elif n.getKey() < key:
                n.setRight(self.rremove(n.getRight(), key))
            else:
                if n.getRight() is None:
                    return n.getLeft()
                if n.getLeft() is None:
                    return n.getRight()
                mini = self.rmin(n.getRight())
                mini.setLeft(n.getLeft())
                n = n.getRight()
        n.setSize(self.nsize(n))
        return n

    # name: min
    # assumptions: exists
    # input: None
    # output: None or the minimum key
    def min(self):
        return self.rmin(self.root).getKey()

    # recursive element of min()
    def rmin(self, n):
        if n is None:
            return n
        elif n.getLeft() is None:
            return n
        else:
            return self.rmin(n.getLeft())

    # name: man
    # assumptions: exists
    # input: None
    # output: None or the maximum key
    def max(self):
        return self.rmax(self.root).getKey()

    # recursive element of max
    def rmax(self, n):
        if n is None:
            return n
        elif n.getRight() is None:
            return n
        else:
            return self.rmax(n.getRight())

    # name: repr
    # assumptions: exists
    # input: None
    # output: the ordered key values with brackets encasing them
    def __repr__(self):
        temp = self.rrepr(self.root)
        temp = temp[0: len(temp) - 2]
        return "{" + temp + "}"

    # recursive element of repr/toString
    def rrepr(self, n):
        if n is None:
            return ""
        return self.rrepr(n.getLeft()) + str(n.getKey()) + "=" + str(n.getValue()) + ", " + self.rrepr(n.getRight())

    # method used for testing stuff
    def getRoot(self):
        return self.root
