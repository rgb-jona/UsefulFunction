def RecursiveSearch(string, searchString):
    """This function returns all appearances of searchString in string and returns them as list"""
    stringIndex = string.find(searchString)
    if stringIndex >= 0:
        # search for further appearances of searchString in string by recursively calling the RecursiveSearch function
        # with trimmed string from stringIndex+1 to end, to prevent finding same string as before again
        resultList = RecursiveSearch(string[stringIndex + 1:], searchString)

        # since the string was trimmed the stored indices need to be corrected
        for counter in range(0,len(resultList)):
            resultList[counter] += stringIndex + 1

        # insert is used instead of append to ensure that the indices sorted from lowest to highest
        resultList.insert(0,stringIndex)
        return resultList
    else:
        # returning empty array so it can be filled with the results of the function calls before
        return []

if __name__ == "__main__":
    print(RecursiveSearch('this is a test','t'))
