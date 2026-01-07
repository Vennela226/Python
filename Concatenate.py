def concatenate_strings(*args):
    result = ""
    for string in args:
        result += string
    return result
concatenated = concatenate_strings("Hello", " ", "world", "!")
print(concatenated)