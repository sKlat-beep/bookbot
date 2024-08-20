def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_book_words(text)
    character_count = count_text_characters(text)
    sorted_characters = sort_list(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    for char in sorted_characters:
        if char["character"].isalpha():
            print(f"The '{char['character']}' character was found {char['count']} times")
        else:
            print(f"The '{char['character']}' character was found {char['count']} times but is not a letter")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_book_words(text):
    words = text.split()
    return len(words)

def count_text_characters(text):
    counted = {}
    for i in text.lower():
        if i not in counted:
            counted[i] = 1
        else:
            counted[i] += 1
    return counted

def sort_on(counted):
    return counted["count"]

def sort_list(num_chars):
    sorted_list = []
    for c in num_chars:
        sorted_list.append({"character": c, "count": num_chars[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
