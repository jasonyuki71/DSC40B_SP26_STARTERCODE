import dsc40graph

def slc(graph, d, k):
    '''
    Performs single linkage clustering using Kruskal's algorithm.
    '''
    clusters = [{node} for node in graph.nodes] 
    edges = sorted(graph.edges, key=d)
    
    for edge in edges:
        u, v = edge
        cluster_u = None
        cluster_v = None
        
        for cluster in clusters:
            if u in cluster:
                cluster_u = cluster
            if v in cluster:
                cluster_v = cluster

        if cluster_u == cluster_v:
            continue

        new_cluster = cluster_u | cluster_v
        clusters.remove(cluster_u)
        clusters.remove(cluster_v)
        clusters.append(new_cluster)

        if len(clusters) == k:
            break
    
    return frozenset(frozenset(cluster) for cluster in clusters)
