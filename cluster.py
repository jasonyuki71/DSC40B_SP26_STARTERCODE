def cluster(graph, weights, level):
    '''
    Clusters a graph based on similarity.
    '''
    visit = set()
    cluster = set()
    
    for node in graph.nodes:
        if node not in visit:
            component = set()
            pending = [node]
            visit.add(node)
            
            while pending:
                u = pending.pop()
                component.add(u)
                
                for v in graph.neighbors(u):
                    if weights(u, v) >= level and v not in visit:
                        visit.add(v)
                        pending.append(v)
            
            cluster.add(frozenset(component))
    
    return frozenset(cluster)
