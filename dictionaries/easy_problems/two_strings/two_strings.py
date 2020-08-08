# Solved in one go!
def twoStrings(s1, s2):
    # O(n) - Feed strings into set
    string1Set = set(s1)
    string2Set = set(s2)

    commonSubString = string1Set.intersection(string2Set)

    if len(commonSubString) != 0: return "YES"
    else: return "NO"

if __name__ == "__main__":
    pass