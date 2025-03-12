# Your Student ID:  240543022
# Your Name and Surname:  IBRAHIM HALIL SIYLI
def convert_temp(value, to_fahrenheit=True):
    return (value * 9/5 + 32) if to_fahrenheit else (value - 32) * 5/9

def main():
    choice = input("Choose conversion: 1) C to F  2) F to C: ")
    temp = float(input("Enter temperature: "))
    result = convert_temp(temp, to_fahrenheit=(choice == "1"))
    unit = "°F" if choice == "1" else "°C"
    print(f"Converted temperature: {result:.2f}{unit}")

if __name__ == "__main__":
    main()
