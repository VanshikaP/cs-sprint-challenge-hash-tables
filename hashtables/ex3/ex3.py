def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    # put all elements with their counts in a map
    countsMap = {}

    for values in arrays:
        for item in values:
            if item in countsMap:
                countsMap[item] += 1
            else:
                countsMap[item] = 1
    
    # get all items with count same as number of elements in arrays
    for item in countsMap:
        if countsMap[item] is len(arrays):
            result.append(item)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
