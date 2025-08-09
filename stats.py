def word_count(str):
    words = str.split()
    return len(words)

def char_count(str):
    char_list = list(str)
    char_set = set(char_list)
    count = {}
    for char in char_set:
        count[char] = char_list.count(char)
    return count
