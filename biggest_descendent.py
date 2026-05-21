import dsc40graph

def biggest_descendent(graph, root, value, biggest=None):
    '''
    Finds the biggest descendent of each node in a tree.
    '''
    if biggest is None:
        biggest = {}

    max_value = value[root]

    for neighbor in graph.neighbors(root):
        child_biggest = biggest_descendent(graph, neighbor, value, biggest)
        max_value = max(max_value, child_biggest[neighbor])
    
    biggest[root] = max_value
    
    return biggest
