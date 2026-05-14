def assign_good_and_evil(graph):
    '''
    Assigns good and evil labels to nodes in a graph.
    '''
    labels = {}
    
    for start in graph.nodes:
        if start not in labels:
            labels[start] = 'good'
            pending = [start]
            while len(pending) > 0:
                node = pending.pop(0)
                for neighbor in graph.neighbors(node):
                    if labels[node] == 'good':
                        opposite = 'evil'
                    else:
                        opposite = 'good'
                    if neighbor not in labels:
                        labels[neighbor] = opposite
                        pending.append(neighbor)
                    elif labels[neighbor] == labels[node]:
                        return None

    return labels
