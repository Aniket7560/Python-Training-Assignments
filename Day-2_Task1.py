# 1. Filter Even Numbers
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# 2. Character Frequency
def count_characters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

# 3. Palindrome Check
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

# 4. Average of *args
def calculate_average(*args):
    if not args: return 0
    return sum(args) / len(args)

# 5. Common Elements
def find_common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

# --- TESTING THE FUNCTIONS (This produces the output) ---

print("Even Numbers:", filter_even_numbers([1, 2, 3, 4, 5, 6]))
# Output: [2, 4, 6]

print("Char Counts:", count_characters("hello"))
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print("Is 121 a Palindrome?:", is_palindrome(121))
# Output: True

print("Average:", calculate_average(10, 20, 30, 40))
# Output: 25.0

print("Common Elements:", find_common_elements([1, 2, 3], [2, 3, 4]))
# Output: [2, 3]
