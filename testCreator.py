#!usr/bin/python python3

from itertools import permutations
import random

class Node():

    def __init__(self, name):
        
        self.name = name

    def __str__ (self):

        return self.name

def printMatrix(matrix):
    for rows in matrix:
        for nodes in rows:
            print(nodes, end=',')
        print("")

def main():
    
    SIZE = 100
    STR_RAND = "ABCDEFGHI"
    filename = "test.txt"
    x = 0
    
    names = ["".join(s) for s in permutations(STR_RAND)]
    array_nodes = []
    
    for _ in range(SIZE):
        temp = []
        for _ in range(SIZE):
            temp.append(Node(names[x]))
            x += 1
        array_nodes.append(temp)
    #print(names)

    with open(filename, "w") as fopen:

        for i in range(SIZE):
            for j in range(SIZE-1):
                
                fopen.write("{},{},{}\n".format(array_nodes[i][j].name, array_nodes[i][j+1].name, random.randint(1,100)))
                fopen.write("{},{},{}".format(array_nodes[j][i].name, array_nodes[j+1][i].name, random.randint(1,100)))
                #if i != SIZE-1 and j !=SIZE-2:
                fopen.write("\n")
            
    #printMatrix(array_nodes)
    #print(array_nodes)
    

if __name__ == "__main__":
    main()
