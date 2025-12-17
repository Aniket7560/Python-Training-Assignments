def count_chars(s):
    vowels = "aeiouAEIOU"
    vowels_count = consonants_count = digits_count = special_count = 0

    for char in s:
        if char.isdigit():
            digits_count += 1
        elif char in vowels:
            vowels_count += 1
        elif char.isalpha():
            consonants_count += 1
        else:
            special_count += 1

    return vowels_count, consonants_count, digits_count, special_count

string = input("Enter a string: ")
vowels, consonants, digits, special = count_chars(string)
print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}, Special Characters: {special}")
