# Your Student ID:  240543022
# Your Name and Surname:  IBRAHIM HALIL SIYLI
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return "Error: Division by zero" if b == 0 else a / b
    else:
        return "Error: Invalid operation"

def main():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Enter operation (+, -, *, /): ")
            print("Result:", calculate(a, b, op))
        except ValueError:
            print("Error: Please enter valid numbers")
        if input("Do another calculation? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
