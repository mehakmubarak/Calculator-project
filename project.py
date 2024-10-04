def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by 0 is not allowed"
    return a / b

print("Welcome to simple calculator made by Mehak Mubarak")
print("""Please select from below options:
      Select A for Addition
      Select B for Subtraction
      Select C for Multiplication
      Select D for Division""")

Answer = input("Please select an option (A, B, C, or D): ").upper()
NUM_1 = float(input("Please enter your first number: "))
NUM_2 = float(input("Please enter your second number: "))

if Answer == "A":
    print(f"Your Answer after Addition: {add(NUM_1, NUM_2)}")
elif Answer == "B":
    print(f"Your Answer after Subtraction: {minus(NUM_1, NUM_2)}")
elif Answer == "C":
    print(f"Your Answer after Multiplication: {multiply(NUM_1, NUM_2)}")
elif Answer == "D":
    print(f"Your Answer after Division: {division(NUM_1, NUM_2)}")
else:
    print("Please input a valid option (A, B, C, or D)")
