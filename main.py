def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    character_dict = character_counter(text)
    character_list = character_report(character_dict)
    report_print(character_list, num_words)

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

def sort_on(dict):
    return dict["num"]

def character_report(dict):
    character_list = []
    for entry in dict:
        if entry.isalpha():
            char_entry = {
                "char" : entry,
                "num": dict[entry]
            }
            character_list.append(char_entry)
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def report_print(character_list, word_count):
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for character in character_list:
        print(f"The '{character['char']}' was found {character['num']} times")
    print("--- End report ---")

main()

