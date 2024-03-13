def is_pangram(sentence):
    lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
    seen_letters = set()
    for char in sentence.lower():
        if char.isalpha() and char in lowercase_alphabet:
            seen_letters.add(char)
    return len(seen_letters) == 26


# Test cases
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("Pack my box with five dozen liquor jugs"))  # True
print(is_pangram("A short sentence"))
