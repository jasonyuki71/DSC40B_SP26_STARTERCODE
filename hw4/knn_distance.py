import random

def knn_distance(arr, q, k):
    """Compute the kth nearest point and the distance to it."""
    pairs = [(abs(x - q), x) for x in arr]

    def quickselect(lst, k):
        if len(lst) == 1:
            return lst[0]
        
        pivot = lst[0]
        left = [x for x in lst if x[0] < pivot[0]]
        mid = [x for x in lst if x[0] == pivot[0]]
        right = [x for x in lst if x[0] > pivot[0]]
        
        if k <= len(left):
            return quickselect(left, k)
        elif k <= len(left) + len(mid):
            return mid[0] 
        else:
            return quickselect(right, k - len(left) - len(mid))
    
    distance, point = quickselect(pairs, k)
    return (distance, point)
