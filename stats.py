def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"


def get_num_char(text):
    num_char = {}
    for char in text:
        char = char.lower()
        num_char[char] = num_char.get(char, 0) + 1
    return num_char


def sort_dict(word_dict):
    return word_dict["num"]


def get_report(word_dict):
    characters = []
    for word, num in word_dict.items():
        characters.append({"char": word, "num": num})
    characters.sort(key=sort_dict, reverse=True)
    return characters
