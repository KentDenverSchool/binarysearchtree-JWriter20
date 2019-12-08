from TreeNode import TreeNode


# add header and method headers
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def size(self):
        return self.root.getSize()

    def nsize(self, n):
        sum = 1
        if n.getLeft() is not None:
            sum += n.getLeft().getSize()
        if n.getRight() is not None:
            sum += n.getRight().getSize()
        return sum


    def isEmpty(self):
        if self.size() is 0:
            return True
        else:
            return False

    def put(self, key, value):
        self.root = self.rput(self.root, key, value)

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

    def get(self, key):
        return self.rget(self.root, key);

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

    def contains(self, key):
        if self.get(key) is not None:
            return True
        else:
            return False

    def remove(self, key):
        v = self.get(key)
        self.root = self.rremove(self.root, key)
        print(self.root)
        return v

    def rremove(self, n, key):
        if n is None:
            return None
        else:
            if n.getKey() < key:
                n.setLeft(self.rremove(n.getLeft(), key))
            elif n.getKey() > key:
                n.setRight(self.rremove(n.getRight(), key));
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

    def min(self):
        return self.rmin(self.root).getKey()

    def rmin(self, n):
        if n is None:
            return n
        elif n.getLeft() is None:
            return n
        else:
            return self.rmin(n.getLeft())

    def max(self):
        return self.rmax(self.root).getKey()

    def rmax(self, n):
        if n is None:
            return n
        elif n.getRight() is None:
            return n
        else:
            return self.rmax(n.getRight())

    def __repr__(self):
        temp = self.rrepr(self.root)
        temp = temp[0: len(temp) - 2]
        return "{" + temp + "}"

    def rrepr(self, n):
        if n is None:
            return ""
        return self.rrepr(n.getLeft()) + str(n.getKey()) + "=" + str(n.getValue()) + ", " + self.rrepr(n.getRight())

    def getRoot(self):
        return self.root
