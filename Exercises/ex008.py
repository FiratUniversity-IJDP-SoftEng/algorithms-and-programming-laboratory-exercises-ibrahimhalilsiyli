# Your Student ID: 240543022
# Your Name and Surname:IBRAHIM HALIL SIYLI
_number = int(input("Enter a number to specify the number of rows for the pyramid pattern:  "))

for i in range(1, _number+1):
    print(" " * (_number - i) + "*" * (2 * i - 1))
