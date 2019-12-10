# Author: Jake Writer
# purpose: Tests the methods of the previously made BinarySearchTree
# Date: 12/8/19
import sys

from BinarySearchTree import BinarySearchTree

if __name__ == '__main__':
    newTree = BinarySearchTree()
    results = "_________Testing BinarySearchTree__________\n"

    with open("TestValuesFile.txt") as f:
        for line in f:
            line = line.split("   ")

    # testing put()
    results += "Testing put():\n\tExpected output: {3=3, 14=2, 15=1, 16=3, 18=5, 19=3}\n\tActual output: "
    for i in range(0, len(line), 2):
        newTree.put(int(line[i]), int(line[i+1]))
    results += str(newTree) + "\n"


    # testing get()
    results += "Testing get():\n\tExpected output: 5\n\tActual output: "
    results += str(newTree.get(int(line[4]))) + "\n"

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
    results += str(newTree.contains(int(line[0]))) + "\n"

    # testing toSting()/repr()
    results += "Testing repr():\n\tAlready passed test when used in put\n"

    try:
        # testing remove()
        results += "Testing remove():\n\tExpected output: {}\n\tActual output: "
        for i in range(0, len(line), 2):
            newTree.remove(int(line[i]))
        returnValue = str(newTree) + "\n"
    except IndexError as e:
        returnValue = e
    results += str(returnValue)

    # testing isEmpty()
    results += "Testing isEmpty() Again:\n\tExpected output: True\n\tActual output: "
    results += str(newTree.isEmpty()) + "\n"

    try:
        f = open(input("Name of test file: ") + '.txt', 'w')
        sys.stdout = f
        f.write(results)
    except KeyboardInterrupt as e:
        print("\nProblems writing to log file")
