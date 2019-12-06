#add quick header
from BinarySearchTree import BinarySearchTree

if __name__ == '__main__':
    newTree = BinarySearchTree()
    # testing put()
    print("Testing put")
    newTree.put(15, 1)
    print(newTree)
    newTree.put(14, 2)
    print(newTree)
    newTree.put(18, 2)
    print(newTree)
    newTree.put(3, 3)
    print(newTree)
    newTree.put(16, 3)
    print(newTree)
    newTree.put(18, 5)
    newTree.put(19, 3)
    print(newTree)

    # testing get()
    print(newTree.get(18))

    #testing size()
    print("testing size")
    print(newTree.size())

    #testing isEmpty()
    print('testing isEmpty ')
    print(newTree.isEmpty())
    
    '''
    # testing remove()
    print("testing remove")
    i = 0
    itemsToRemove = [15, 18, 16, 3, 19, 14]
    while newTree.size() is not 0:
        print(newTree.size())
        print(newTree)
        print(itemsToRemove[i])
        newTree.remove(newTree.get(itemsToRemove[i]))
        i += 1
'''
    # testing isEmpty()
    print('testing isEmpty ')
    print(newTree.isEmpty())

    #testing contains()

    #testing min()

    #testing max()

    #testing toSting()/repr()