import math
from typing import Union

def addition(a: float, b: float) -> float:
    """Returns the sum of a and b."""
    return a + b

def subtraction(a: float, b: float) -> float:
    """Returns the difference of a and b."""
    return a - b    

def multiplication(a: float, b: float) -> float:
    """Returns the product of a and b."""
    return a * b    

def division(a: float, b: float) -> Union[float, str]:
    """Returns the quotient of a divided by b."""
    if b == 0:
        return "Error: Division by zero."
    return a / b

def power(a: float, b: float) -> float:
    """Returns a raised to the power of b."""
    return a ** b

def square_root(a: float) -> Union[float, str]:
    """Returns the square root of a."""
    if a < 0:
        return "Error: Negative value."
    return round(math.sqrt(a), 6)

def modulus(a: float, b: float) -> Union[float, str]:
    """Returns the remainder of a divided by b."""
    if b == 0:
        return "Error: Division by zero."
    return a % b

def logarithm(a: float, base: float) -> Union[float, str]:
    """Returns the logarithm of a with the specified base."""
    if a <= 0 or base <= 0 or base == 1:
        return "Error: Invalid input."
    return round(math.log(a, base), 6)

def factorial(n: int) -> Union[int, str]:
    """Returns the factorial of a non-negative integer n."""
    if n < 0:
        return "Error: Negative value."
    return math.factorial(n)   

def floor_division(a: float, b: float) -> Union[float, str]:
    """Returns the floor division of a by b."""
    if b == 0:
        return "Error: Division by zero."
    return a // b   

def sine(angle: float) -> float:
    """Returns the sine of an angle in degrees."""
    return round(math.sin(math.radians(angle)), 6)    

def cosine(angle: float) -> float:
    """Returns the cosine of an angle in degrees."""
    return round(math.cos(math.radians(angle)), 6)

def tangent(angle: float) -> Union[float, str]:
    """Returns the tangent of an angle in degrees."""
    cos_val = math.cos(math.radians(angle))
    if abs(cos_val) < 1e-12:
        return "Error: Undefined."
    return round(math.tan(math.radians(angle)), 6)

def exponential(a: float) -> Union[float, str]:
    """Returns e raised to the power of a."""
    try:
        return round(math.exp(a), 6)
    except OverflowError:
        return "Error: Overflow."

def sec(angle: float) -> Union[float, str]:
    """Returns the secant of an angle in degrees."""
    cos_val = cosine(angle)
    if cos_val == 0 or abs(cos_val) < 1e-12:
        return "Error: Undefined."
    return round(1 / cos_val, 6)

def cosec(angle: float) -> Union[float, str]:
    """Returns the cosecant of an angle in degrees."""
    sin_val = sine(angle)
    if sin_val == 0 or abs(sin_val) < 1e-12:
        return "Error: Undefined."
    return round(1 / sin_val, 6)

def cot(angle: float) -> Union[float, str]:   
    """Returns the cotangent of an angle in degrees."""
    tan_val = tangent(angle)
    if isinstance(tan_val, str) or tan_val == 0:
        return "Error: Undefined."
    return round(1 / tan_val, 6)

def get_float_input(prompt: str) -> float:
    """Safely prompts the user for a floating point number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_int_input(prompt: str) -> int:
    """Safely prompts the user for a non-negative integer."""
    while True:
        try:
            val = int(input(prompt))
            return val
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def print_menu():
    """Prints the calculator options menu."""
    print("\nWelcome to the Advanced Calculator!")
    print("Select operation:")
    print("+. Addition")
    print("-. Subtraction")
    print("*. Multiplication")
    print("/. Division")
    print("**. Power")
    print("sqrt. Square Root")
    print("%. Modulus") 
    print("log. Logarithm")
    print("!. Factorial")
    print("//. Floor Division") 
    print("sin. Sine")
    print("cos. Cosine")
    print("tan. Tangent")
    print("exp. Exponential")
    print("sec. Secant")
    print("cosec. Cosecant")
    print("cot. Cotangent")
    print("exit. Exit")

def main():
    print_menu()
    
    single_num_ops = {"sqrt", "exp"}
    trig_ops = {"sin", "cos", "tan", "sec", "cosec", "cot"}
    two_num_ops = {"+", "-", "*", "/", "**", "%", "log", "//"}

    while True:
        choice = input("\nEnter choice: ").strip().lower()
        if choice == "exit":
            print("Exiting the calculator. Goodbye!")
            break   

        if choice in single_num_ops:
            num = get_float_input("Enter number: ")
            if choice == "sqrt":
                print("Result:", square_root(num))
            elif choice == "exp":
                print("Result:", exponential(num))

        elif choice == "!":
            num = get_int_input("Enter non-negative integer: ")
            print("Result:", factorial(num))

        elif choice in trig_ops:
            angle = get_float_input("Enter angle in degrees: ")
            if choice == "sin":
                print("Result:", sine(angle))
            elif choice == "cos":
                print("Result:", cosine(angle))
            elif choice == "tan":
                print("Result:", tangent(angle))
            elif choice == "sec":
                print("Result:", sec(angle))
            elif choice == "cosec":
                print("Result:", cosec(angle))
            elif choice == "cot":
                print("Result:", cot(angle))

        elif choice in two_num_ops:
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            if choice == "+":
                print("Result:", addition(num1, num2))
            elif choice == "-":
                print("Result:", subtraction(num1, num2))
            elif choice == "*":
                print("Result:", multiplication(num1, num2))
            elif choice == "/":
                print("Result:", division(num1, num2))
            elif choice == "**":
                print("Result:", power(num1, num2))
            elif choice == "%":
                print("Result:", modulus(num1, num2))
            elif choice == "log":
                print("Result:", logarithm(num1, num2))
            elif choice == "//":
                print("Result:", floor_division(num1, num2))

        else:
            print("Error: Invalid input.")

if __name__ == "__main__":
    main()