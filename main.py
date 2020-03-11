from node import Node

node0 = Node(0)     #creates instances of node and identifies each one with a number
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node0.paths = [node2, node1]        #sets the edges between nodes by setting path attributes of nodes
node1.paths = [node2]
node2.paths = [node4, node3]
node3.paths = [node6]
node4.paths = [node6, node5]
node5.paths = [node4]
node6.paths = []

graph = [node0, node1, node2, node3, node4, node5, node6]       # defines a graph as a list of nodes
potential_simple_paths =[]      #paths that could be simple
illegal_paths = []      #paths in potential list that have a cycle
simple_paths = []       #potential simple paths with cycle paths removed; all legal simple paths
prime_paths = []        #all simple paths that are not subpaths of any other simple path

def add_nodes_to_simple_paths(graph):       #since each node by itself is a simple path, they are added the the list
    global potential_simple_paths
    for node in graph:
        potential_simple_paths.append([node.number])

add_nodes_to_simple_paths(graph)

def find_potential_simple_paths(node, track):
    global potential_simple_paths
    for next_node in node.paths:        #checks all paths from a given node
        if((next_node not in track) or (next_node.number == track[0].number)):      #only considers new nodes or the first one in the path to be added to a potential simple path
            track.append(next_node)
            temp_track = []
            for node in track:
                temp_track.append(node.number)
            potential_simple_paths.append(temp_track)       #adds path to list of potential simple paths
            find_potential_simple_paths(next_node, track)       #recursively checks all nodes reachable from given node
    track.remove(track[len(track)-1])       #if a deadend is reached, the path is backtracked to explore other options

find_potential_simple_paths(node0, [node0])     #finds all potential simple paths starting from each node in the graph
find_potential_simple_paths(node1, [node1])
find_potential_simple_paths(node2, [node2])
find_potential_simple_paths(node3, [node3])
find_potential_simple_paths(node4, [node4])
find_potential_simple_paths(node5, [node5])
find_potential_simple_paths(node6, [node6])

print("Potential Simple Paths: ")
print(potential_simple_paths)

def find_illegal_paths(potentialsimplepaths):       #finds paths in potential simple paths that have a cycle not including the first and last node
    for i in range (len(potentialsimplepaths)):
        path = potentialsimplepaths[i]
        if len(path) != len(set(path)):
            if(path[0] != path[len(path)-1]):
                illegal_paths.append(path)

find_illegal_paths(potential_simple_paths)

print("Illegal Paths: ")
print(illegal_paths)

for path in illegal_paths:      #removes illegal paths from potential list, to form simple paths
    potential_simple_paths.remove(path)

simple_paths = potential_simple_paths

print("There are", len(simple_paths), " Simple Paths: ")
print(simple_paths)

def if_subset(path1, path2):        #checks for pubpaths in simple paths
    for i in range(len(path2)-len(path1)+1): 
        for j in range(len(path1)): 
            if path2[i + j] != path1[j]: 
                break
        else:
            if(path1 != path2): 
                return True
    return False
            
def is_prime_path(path, simplepaths):       #checks if a given simple path is a prime path
    for i in range (len(simplepaths)):
        potential_subset = simplepaths[i]
        if(if_subset(path, potential_subset) == True):
            return False
    return True

def find_prime_paths(simplepaths):      #checks if all paths in simple paths are prime paths
    global prime_paths
    for i in range (len(simplepaths)):
        potential_primepath = simplepaths[i]
        if(is_prime_path(potential_primepath, simplepaths) == True):
            prime_paths.append(potential_primepath)

find_prime_paths(simple_paths)
print("There are", len(prime_paths), "Prime Paths: ")
print(prime_paths)