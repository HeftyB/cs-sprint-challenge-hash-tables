# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    newdict = {}

    for filepath in files:
        split = filepath.split("/")
        if split[-1] not in newdict:
            newdict[split[-1]] = []
        newdict[split[-1]].append(filepath)

    result = []

    for q in queries:
        if q in newdict:
            for r in newdict[q]:
                result.append(r)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
