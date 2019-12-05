import TreeNode
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.s = 0

    def size(self):
        return self.s

    def isEmpty(self):
        if self.s is 0:
            return True
        else:
            return False
    def put(self, key, value):
        self.root = self.put(self.root, key, value)

    def put(self, n, key, value):
        if n is None:
            self.root = TreeNode(key, value)
            self.s += 1
            return self.root
        if n.getKey() < key:
            if n.getLeft() is None:
                newNode = TreeNode(key,value)
                n.setLeft(newNode)
                self.s += 1
            else:
                n.setLeft(self.put(n.getLeft(), key, value))
        if n.getKey() > key:
            if n.getRight() is None:
                newNode = TreeNode(key, value)
                n.setRight(newNode)
                self.s += 1
            else:
                n.setRight(self.put(n.getRight(), key, value))


    def get(self, key):
        return self.get(self.root, key);

    def get(self, n, key):
        if n is None:
            return None
        if n.getKey() < key:
            if n.getLeft() is None:
                return None
            else:
                n.setLeft(self.get(n.getLeft(), key))
        if n.getKey() > key:
            if n.getRight() is None:
                return None
            else:
                n.setRight(self.get(n.getRight(), key))
        if n.getKey == key:
            return n

    def contains(self, key):
        if(self.root.get(key) is not None):
            return True
        else:
            return False


    def remove(self, key):

    def remove(self, n, key):

    def min(self):
        return self.min(self.root).getKey()

    def min(self, n):
        if n is None:
            return n
        elif n.getLeft() is None:
            return n
        else:
            return n.getLeft()


    def max(self):
        return self.max(self.root).getKey()

    def max(self, n):
        if n is None:
            return n
        elif n.getRight() is None:
            return n
        else:
            return n.getRight()


    def __repr__(self):
        temp = repr(self.root)
        temp = temp.substring(0, temp.length() - 2)
        return "{" + temp + "}"

    def __repr__(self, n):
        if n == None:
            return ""
        return repr(n.getLeft()) + n.getKey() + "=" + n.getValue() + ", " + repr(n.getRight())
