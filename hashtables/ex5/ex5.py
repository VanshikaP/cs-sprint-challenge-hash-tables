# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    # map file names to their path
    filePathMap = {}
    for path in files:
        address = path.split('/')
        filename = address[len(address) - 1]

        if filename in filePathMap:
            filePathMap[filename].append(path)
        else:
            filePathMap[filename] = [path]
    
    # get paths for filenames in queries
    for filename in queries:
        if filename in filePathMap:
            for path in filePathMap[filename]:
                result.append(path)


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
