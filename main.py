def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    character_dict = character_counter(text)
    print(num_words)
    print(character_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book):
    words = book.split()
    return len(words)

def character_counter(book):
    letter_count = {}
    uncapitalized_book = book.lower()
    for s in uncapitalized_book:
        character_amount = 0
        if s not in letter_count:
            letter_count[s] = character_amount
        letter_count[s] += 1
    return letter_count

main()

