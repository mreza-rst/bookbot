def word_count(str):
    words = str.split()
    return len(words)

def char_count(str):
    lowercased = str.lower()
    char_list = list(lowercased)
    char_set = set(char_list)
    count = {}
    for char in char_set:
        count[char] = char_list.count(char)
    return count
