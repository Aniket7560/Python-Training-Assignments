try:
    s = "Hello"
    s[0] = 'h'  # Attempting to change the string
except TypeError:
    print("Strings are immutable in Python!")
