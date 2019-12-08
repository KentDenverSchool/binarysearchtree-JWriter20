#add quick header
import sys

from BinarySearchTree import BinarySearchTree

if __name__ == '__main__':
    newTree = BinarySearchTree()
    results = "_________Testing BinarySearchTree__________\n"
    # testing put()
    results += "Testing put():\n\tExpected output: {3=3, 14=2, 15=1, 16=3, 18=5, 19=3}\n\tActual output: "
    newTree.put(15, 1)
    newTree.put(14, 2)
    newTree.put(18, 2)
    newTree.put(3, 3)
    newTree.put(16, 3)
    newTree.put(18, 5)
    newTree.put(19, 3)
    results += str(newTree) + "\n"


    # testing get()
    results += "Testing get():\n\tExpected output: 5\n\tActual output: "
    results += str(newTree.get(18)) + "\n"

    #testing size()
    results += "Testing size():\n\tExpected output: 6\n\tActual output: "
    results += str(newTree.size()) + "\n"

    #testing isEmpty()
    results += "Testing isEmpty():\n\tExpected output: False\n\tActual output: "
    results += str(newTree.isEmpty()) + "\n"

    # testing min()
    results += "Testing min():\n\tExpected output: 3\n\tActual output: "
    results += str(newTree.min()) + "\n"

    # testing max()
    results += "Testing max():\n\tExpected output: 19\n\tActual output: "
    results += str(newTree.max()) + "\n"

    # testing contains()
    results += "Testing contains():\n\tExpected output: True\n\tActual output: "
    results += str(newTree.contains(15)) + "\n"

    # testing toSting()/repr()
    results += "Testing repr():\n\tAlready passed test when used in put\n"

    newTree.remove(15)
    print(newTree)
    try:
        # testing remove()
        results += "Testing remove():\n\tExpected output: {}\n\tActual output: "
        i = 0
        itemsToRemove = [15, 18, 16, 3, 19, 14]
        while newTree.size() is not 0:
            newTree.remove(newTree.get(itemsToRemove[i]))
            i += 1
        returnValue = str(newTree) + "\n"
    except IndexError as e:
        returnValue = e
    results += str(returnValue) + "\n"

    # testing isEmpty()
    results += "Testing isEmpty() Again:\n\tExpected output: True\n\tActual output: "
    results += str(newTree.isEmpty()) + "\n"

    try:
        f = open(input("Name of test file: ") + '.txt', 'w')
        sys.stdout = f
        f.write(results)
    except():
        print("Problems writing to log file")
