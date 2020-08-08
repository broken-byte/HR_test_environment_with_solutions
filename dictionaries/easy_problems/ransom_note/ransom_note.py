'''
Solved on first attempt! :D
'''
def checkMagazine(magazine, note):
    # O(N) - MagazineMap = dictionary of key = word, value = number of instances of word
    magazineMap = {}
    for word in magazine:
        if word in magazineMap:
            magazineMap[word] += 1
        else:
            magazineMap[word] = 1

    # O(N) check words in note against magazineMap
    for word in note:
        if word not in magazineMap: 
            return "No"

        elif magazineMap[word] == 0:
            return "No"

        else: magazineMap[word] -= 1
    
    # O(N + N) ~= O(2N) ~= O(N)
    return "Yes"

if __name__ == "__main__":
    pass