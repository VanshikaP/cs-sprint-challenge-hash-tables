def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    # map of values
    valuesMap = {}
    
    for i in range(len(a)):
        valuesMap[a[i]] = i
    
    for value in a:
        if -value in valuesMap and value > 0:
            result.append(value)
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
