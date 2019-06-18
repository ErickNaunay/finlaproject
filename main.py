# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:11:40 2019

@author: Morgan Hooker & Erick Naunay
Python programming

"""
import os
import sys

FILE_LOCATION = os.path.join(os.path.dirname(__file__), "test.txt")

class MapGraph():
    
    #
    #constructor
    #
    def __init__(self):
        
        #Map dictionary
        self._data = {}
        self._cities = {}
        
        self.visitedVertex = []
        self.univistedVertex = []
        
        self.matrix = {}

    #
    #function that adds a new node verifying its existance
    #initialize a list in the node value
    #
    def add_node(self, key):
        
        if key in self._data.keys():
            raise ValueError('Duplicate key!')
            
        self._data[key] = []
    
    #
    #Add neighbor city to a city
    #Valides existance and do not override
    #Use a dictionary to storage name and weight
    #
    def add_edge(self, to, _from):
        
        #verify if both nodes exist
        if not to["name"] in self._data.keys():
            raise ValueError('to node does not exist!')
            
        elif not _from["name"] in self._data.keys():
            raise ValueError('from node does not exist!')
        
        #verify if the conection to-from already exists (dont override)
        if _from["name"] not in self._data[to["name"]]:
            self._data[to["name"]].append(_from)
            
        if to["name"] not in self._data[_from["name"]]:
            self._data[_from["name"]].append(to)
        else:
            print("{} and you are already friends".format(to))
    
    #Print the map network       
    def __str__(self):
        
        result= ""
        
        for key, value in self._data.items():
            for v in value:
                result += "{} -> {}\n".format(key,v)
                
        return result
    
    #Comparation override method
    def __contains__(self, obj):
        
        return obj in self._data.keys()
    
    #Algorithm to find the shortest path from a starting node to the end node
    def shortest_path(self, start, end):
        
        #two data structure that will keep track of the cities tranversed
        self.univistedVertex = []
        self.visitedVertex = []
        
        #Verify if the start and end cities are in the map
        if not start in self._data.keys():
            return -1
        if not end in self._data.keys():
            return -1
        
        #clean up the data structure used for the algorithm
        #"Matrix" DS, a dictionary an a list a value, city : [distance, pevious node]
        #The distance is set to infinity and the previous node to None
        #Distance of the start node is set to zero
        for key in self.matrix.keys():
            if key == start:
                self.matrix[key][0] = 0
            else:
                self.matrix[key][0] = sys.maxsize
            self.matrix[key][1] = None
            
            self.univistedVertex.append(key) 
        
       
        #Visit all unvisited vertixes
        while len(self.univistedVertex) != 0:
            
            #Get an univisted vertix with the minimum distance
            vertix = self.minVertix()
            
            #print(vertix)
            #print(self.univistedVertex)
            
            #delete the vertix from the unvisited list
            self.univistedVertex.remove(vertix)
            
            #get all the neighbor cities of the vertix 
            for nextCity in self._data[vertix]:
                
                #Does not re-visit neighbors
                if not nextCity in self.visitedVertex:
                    
                    #calculate the distance to the neighbor respect to the start point
                    newDistance = self.matrix[vertix][0] + nextCity["weight"]
                    
                    #if the distance is smaller than the previous distance update it
                    if newDistance < self.matrix[nextCity["name"]][0]:
                        self.matrix[nextCity["name"]][0] = newDistance
                        self.matrix[nextCity["name"]][1] = vertix 
            
            #add the vertiex to the visited list
            self.visitedVertex.append(vertix)
        
        #
        #Search the path from the start to the goal citie
        #
        path = []
        path.append(end)
        
        pathDistance = sys.maxsize

        prev = end
        
        #
        #Transverse all the matrix starting in the goal citie and then viisting the previous value
        #Until it reaches to the start citie
        #
        while pathDistance != 0:
            prev = self.matrix[prev][1]
            path.append(prev)
            pathDistance = self.matrix[prev][0]
        
        #print(path)
        
        #
        #Print graphically the path found
        #
        result = "Path: "

        for index in range(len(path)-1, -1, -1):
            if index != 0:
                result +="{}->".format(path[index])
            else:
                result += "{}\n".format(path[index])
                
        print(result)
        
        print("Cost: {}".format(self.matrix[end][0]))
        
        #print(self.univistedVertex)
        #print(self.visitedVertex)
        #print(self.matrix)
        
    
    #get a unvisited vertix with the minimun distance    
    def minVertix(self):
        
        minValue = sys.maxsize
        minKey = None
        
        for key in self.univistedVertex:
            if self.matrix[key][0] < minValue:
                minValue = self.matrix[key][0]
                minKey = key
        
        return minKey
    
    #
    # Reads the data from files paths
    # Insert into a graph, users and friendship creation
    # User, friendship and posts data
    #
    @classmethod
    def import_file(cls, file_path):
        
        #Create a new graph for the data read
        graph = MapGraph()
        
        with open(file_path, "r") as f:
            lines = [x.strip().split(',') for x in f.readlines()]
        
        #Get all the info for the creation of an user
        
        for line in lines:

            if len(line) != 3:
                raise ValueError("Data from the file is malformed.")
            try:
                int(line[2])
            except ValueError:
                raise ValueError("Data from the file is malformed.")
                
            #Unique user registration
            try:
                
                try:
                    
                    if not line[0] in graph._data.keys():
                        graph.add_node(line[0])
                    if not line[1] in graph._data.keys(): 
                        graph.add_node(line[1])
                        
                except ValueError:
                    print("Duplicate key.")
                
                try:
                    to = {"name": line[0],
                            "weight": int(line[2])                          
                          }
                    _from = {"name": line[1],
                             "weight": int(line[2]) 
                             }

                    graph.add_edge(to, _from)
                
                
                except ValueError:
                    print("Already friends.")
                
            except ValueError:
                
                print("{} has already been registered as city.".format(line[0]))
            
            for key in graph._data.keys():
                graph.matrix[key] = []
                graph.matrix[key].append(sys.maxsize)
                graph.matrix[key].append(None)
            
        return graph

    @classmethod
    def bfs_graph_transversal(cls, graph):
        pass
    #
    # Iterator for username and friends relation
    #
    def __iter__(self):
        for key, value in self._data.items():
            for v in value:
                yield [key,v]


def main():
    
    #graph creation and import data from file
    _map = MapGraph()
    
    _map = MapGraph.import_file(FILE_LOCATION)
    
    #print(_map)
    
    #Menu options
    while True:
        start = input ("Insert start location: ")
        goal = input ("Insert end location: ")

        if (_map.shortest_path(start, goal) == -1):
            print("{} or {} are not register cities.".format(start, goal))
        
        if (input("Quit program? (yes/no): ") == "yes"):
            print("Thanks for using this program.")
            break

if __name__ == '__main__':
    main()