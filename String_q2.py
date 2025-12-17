def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

string = input("Enter a string: ")
print(reverse_words(string))
