# Author: Jake Writer
# purpose: This program creates the node which are used in the creation of a BinarySearchTree
# Date: 12/8/19

class TreeNode:
    def __init__(self, key, value, size):
        self.k = key
        self.s = size
        self.v = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "Node{" + "key=" + str(self.k) + ", value=" + str(self.v) +"}"

    def getKey(self):
        return self.k

    def setKey(self, key):
        self.k = key

    def getValue(self,):
        return self.v

    def setValue(self, value):
        self.v = value

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getSize(self):
        return self.s

    def setSize(self, size):
        self.s = size
