def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    newdict = {}

    for array in arrays:
        for i in array:
            if i not in newdict:
                newdict[i] = 1
            else:
                newdict[i] += 1

    result = []

    for key, value in newdict.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
