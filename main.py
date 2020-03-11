from node import Node

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node0.paths = [node2, node1]
node1.paths = [node2]
node2.paths = [node4, node3]
node3.paths = [node6]
node4.paths = [node6, node5]
node5.paths = [node4]
node6.paths = []

graph = [node0, node1, node2, node3, node4, node5, node6]
potential_simple_paths = [[node0.number], [node1.number], [node2.number], [node3.number], [node4.number], [node5.number], [node6.number]]

def f_s_p(node, track):
    global potential_simple_paths
    #if(node not in potential_simple_paths):
        #potential_simple_paths.append(node.number)
    for next_node in node.paths:
        if((next_node not in track) or (next_node.number == track[0].number)):
            track.append(next_node)
            #potential_simple_paths.append(track)
            
            
            #print(track)
            temp_track = []
            for node in track:
                #print(node.number)
                temp_track.append(node.number)
            #print("")
            #print(temp_track)
            potential_simple_paths.append(temp_track)
            #print(potential_simple_paths)
            f_s_p(next_node, track)
    track.remove(track[len(track)-1])

f_s_p(node0, [node0])
f_s_p(node1, [node1])
f_s_p(node2, [node2])
f_s_p(node3, [node3])
f_s_p(node4, [node4])
f_s_p(node5, [node5])
f_s_p(node6, [node6])


#print(potential_simple_paths)

illegal_paths = []
for i in range (len(potential_simple_paths)):
    #print("path: ")
        #print(potential_simple_paths[i][j])
    path = potential_simple_paths[i]
    #print(path)
    if len(path) != len(set(path)):
        if(path[0] != path[len(path)-1]):
            illegal_paths.append(path)

#print(illegal_paths)

for path in illegal_paths:
    potential_simple_paths.remove(path)

#print(potential_simple_paths)

def is_subset(path1, path2):
        set1 = set(path1)
        set2 = set(path2)
        if((set1.issubset(set2)) and set1 != set2):
            return True
        return False

def if_subset(A, B): 
    for i in range(len(B)-len(A)+1): 
        for j in range(len(A)): 
            if B[i + j] != A[j]: 
                break
        else:
            if(A != B): 
                return True
    return False
            

'''
prime_paths = []
for i in range (len(potential_simple_paths)):
    potential_prime_path = potential_simple_paths[i]
    for j in range (len(potential_simple_paths)):
        potential_subset = potential_simple_paths[j]
        if(is_subset(potential_prime_path, potential_subset)):
            pass
'''
prime_paths = []
def is_prime_path(path, simple_paths):
    for i in range (len(simple_paths)):
        potential_subset = simple_paths[i]
        if(if_subset(path, potential_subset) == True):
            #print(potential_subset)
            return False
    return True

print(is_prime_path([0,2,3,6], potential_simple_paths))

def find_prime_paths(simple_paths):
    global prime_paths
    for i in range (len(simple_paths)):
        potential_primepath = simple_paths[i]
        if(is_prime_path(potential_primepath, simple_paths) == True):
            print(potential_primepath)
            prime_paths.append(potential_primepath)

find_prime_paths(potential_simple_paths)
#print(prime_paths)

#print(prime_paths)

prime = if_subset([5,4,5], [5,4,5])
#print(prime)





'''
list1 = [1, 2, 3]
list2 = [0, 1, 2, 3]
print(list1)
set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)
is_subset = set1.issubset(set2)
print(is_subset)
'''


    