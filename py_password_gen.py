from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from secrets import choice
from json import load

# English words pulled from words_dictionary.json in: https://github.com/dwyl/english-words

def generate_characters_password(password_length: int = 10, use_uppercase: bool = True, use_lowercase: bool = True, use_digits: bool = True, use_symbols: bool = True) -> str:
    """Create password based on random English characters"""
    # create char list
    chars = []
    if use_uppercase:
        chars += list(ascii_lowercase)
    if use_lowercase:
        chars += list(ascii_uppercase)
    if use_digits:
        chars += list(digits)
    if use_symbols:
        chars += list(punctuation)

    # generate password
    password_list = []
    count = password_length
    while count >= 0:
        password_list.append(choice(chars))
        count -= 1
    return "".join(password_list)

def generate_words_password(word_count: int = 5, separator: str = "-") -> str:
    """Create password using random English words"""
    # import English words list
    with open('words_dictionary.json', 'r') as words_dictionary_file:
        words_list = list(load(words_dictionary_file).keys())
    
    # generate password
    password_list = []
    count = word_count
    while count > 0:
        password_list.append(choice(words_list))
        if count > 1:
            password_list.append(separator)
        count -= 1
    return "".join(password_list)