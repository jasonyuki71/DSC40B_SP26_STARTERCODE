def mode(numbers):
    '''
    Efficiently finds the mode of a list of numbers.
    '''
    counts = {}
    best_num = None
    best_count = 0

    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        if counts[num] > best_count:
            best_count = counts[num]
            best_num = num

    return best_num
