def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    posdict = {}
    negdict = {}

    for i in a:
        if i < 0:
            negdict[i * (-1)] = i
        else:
            posdict[i] = i
    
    result = []

    for key, value in posdict.items():
        if key in negdict:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
