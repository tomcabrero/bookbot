import sys
from stats import count_words, count_char, sort_char

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_words = count_words(book)
    num_char = sort_char(count_char(book))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print (f'Found {num_words} total words')
    print("--------- Character Count -------")

    for i in range (0,len(num_char)-1):
        if num_char[i]["char"].isalpha():
            print(f'{num_char[i]["char"]}: {num_char[i]["count"]}')
    print("============= END ===============")

main()