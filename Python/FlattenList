"""This simple function flattens a list"""

def flattenList(inputList):
    functionList = []
    for element in inputList:
        if type(element) is list:
            returnList = flattenList(element)
            functionList += returnList
        else:
            functionList.append(element)
    return functionList

if __name__ == "__main__":
    testList = [1, 2, [1, [4, 3, 4], 1], 1, [1, 2, [1, 2, 3, [[[[1, 2, 3]]], 1]]], 2, [12, 2]]
    print(testList)
    print(flattenList(testList))
