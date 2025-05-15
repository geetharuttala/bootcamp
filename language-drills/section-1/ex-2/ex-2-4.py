text = "hello world"
vowels = {'a', 'e', 'i', 'o', 'u'}
found_vowels = {ch for ch in text if ch in vowels}
print(found_vowels)