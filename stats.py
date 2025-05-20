def count_words (book_text):
    text = book_text.split()
    return len(text)

def analyze (book_text):
    file_contents = book_text.lower()
    dictionary = {}
    for i in file_contents:
        if i.isalpha():
            if i in dictionary:
                dictionary[i] +=1
            else:
                dictionary[i] = 1
    return dictionary


