import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_text (filepath):
    with open(filepath) as text:
        file_contents = text.read()
    return file_contents

from stats import count_words, analyze

def do_list_of_dicts (analyze):
    empty_list = []
    for key, value in analyze.items():
        empty_list.append({"char": key, "num": value})
    empty_list.sort(reverse=True, key=lambda x: x["num"])
    return empty_list




def main ():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in do_list_of_dicts (analyze(book_text)):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    


main ()
