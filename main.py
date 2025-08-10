from stats import sort_chars, word_count, char_count

def file_to_str(filepath):
    with open(filepath) as b:
        return b.read()

def main():
    path = "books/frankenstein.txt"
    book = file_to_str(path)
    num_words = word_count(book)
    num_chars = char_count(book)
    sorted_chars = sort_chars(num_chars)

    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_chars:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")
main()
