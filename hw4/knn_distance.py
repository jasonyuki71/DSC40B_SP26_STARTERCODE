import random

def knn_distance(arr, q, k):
    """Compute the kth nearest point and the distance to it."""
    pairs = [(abs(x - q), x) for x in arr]

    def partition(left, right, pivot_idx):
        pivot = pairs[pivot_idx][0]
        pairs[pivot_idx], pairs[right] = pairs[right], pairs[pivot_idx]
        store = left

        for i in range(left, right):
            if pairs[i][0] < pivot:
                pairs[store], pairs[i] = pairs[i], pairs[store]
                store += 1
        pairs[right], pairs[store] = pairs[store], pairs[right]

        return store

    def quickselect(left, right, k_smallest):
        if left == right:
            return

        pivot_idx = random.randint(left, right)
        pivot_idx = partition(left, right, pivot_idx)
        
        if k_smallest == pivot_idx:
            return            
        elif k_smallest < pivot_idx:
            quickselect(left, pivot_idx - 1, k_smallest)
        else:
            quickselect(pivot_idx + 1, right, k_smallest)

    quickselect(0, len(pairs) - 1, k - 1)
    
    return pairs[k - 1]       
