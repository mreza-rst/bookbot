from stats import word_count, char_count

def file_to_str(filepath):
    with open(filepath) as b:
        return b.read()

def main():
    frankenstein = file_to_str("books/frankenstein.txt")
    num_words = word_count(frankenstein)
    num_chars = char_count(frankenstein)
    print(f"{num_words} words found in the document")
    print(num_chars)

main()
