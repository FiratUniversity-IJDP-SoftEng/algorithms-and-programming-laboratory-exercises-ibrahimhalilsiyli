# Your Student ID:  240543022
# Your Name and Surname:  IBRAHIM HALIL SIYLI
from collections import Counter

_string= input("Enter a string: ")
_string_count = Counter(_string)

print("Character frequencies:")
for i in sorted(_string_count):
    print(f"{i}: {_string_count[i]}")
