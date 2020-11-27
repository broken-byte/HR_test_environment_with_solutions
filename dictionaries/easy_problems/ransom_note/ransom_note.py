'''
Solved on first attempt! :D
'''


def check_magazine(magazine, note):
    # O(N) - MagazineMap = dictionary of key = word, value = number of
    # instances of word
    magazine_map = {}
    for word in magazine:
        if word in magazine_map:
            magazine_map[word] += 1
        else:
            magazine_map[word] = 1

    # O(N) check words in note against magazineMap
    for word in note:
        if word not in magazine_map:
            return "No"

        elif magazine_map[word] == 0:
            return "No"

        else:
            magazine_map[word] -= 1

    # O(N + N) ~= O(2N) ~= O(N)
    return "Yes"


if __name__ == "__main__":
    pass
