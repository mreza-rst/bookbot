from stats import sort_chars, word_count, char_count

def file_to_str(filepath):
    with open(filepath) as b:
        return b.read()

def main():
    frankenstein = file_to_str("books/frankenstein.txt")
    num_words = word_count(frankenstein)
    num_chars = char_count(frankenstein)
    sorted_chars = sort_chars(num_chars)
    print(f"{num_words} words found in the document")
    print(sorted_chars)

main()
