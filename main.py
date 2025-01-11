def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    character_counts = count_characters(text)
    
    character_list = [(key, value) for key, value in character_counts.items()]
    sorted_characters = sorted(character_list, key=lambda x: x[1], reverse=True)
    for i in sorted_characters:
        print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    list_characters = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character.isalpha():
            if character in list_characters:
                list_characters[character] += 1
            else:
                list_characters[character] = 1
    return list_characters


main()
