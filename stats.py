def get_word_count(text: str):
    return len(text.split())

def get_char_count(text: str):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(items):
    return items["num"]

def get_sorted_chars(chars: dict):
    sorted_chars = []
    for char in chars:
        if char.isalpha():
            num = chars[char]
            sorted_chars.append({"char": char, "num": num})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
