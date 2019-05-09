#!usr/bin/python python3

from itertools import permutations

class Node():

    def __init__(self):
        
        self.name = ""
        self.cost = None

        self.up = None
        self.down = None
        self.right = None
        self.left = None

    def __str__ (self):

        return self.name

def printMatrix(matrix):
    for rows in matrix:
        for nodes in rows:
            print(nodes, end=',')
        print("")

def main():
    
    SIZE = 10
    STR_RAND = "ABCDEFGHI"
    array_nodes = [[ Node() for _ in range(SIZE)] for y in range(SIZE)]
    names = ["".join(s) for s in permutations(STR_RAND)]
    ctr = 0

    #print(names)

    for rows in array_nodes:
        for node in rows:
            node.name = names[ctr]
            ctr = ctr + 1
    
    printMatrix(array_nodes)
    #print(array_nodes)
    

if __name__ == "__main__":
    main()
