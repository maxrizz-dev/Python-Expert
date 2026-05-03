# Python Operators Example

a = 10
b = 3

# Arithmetic Operators (+, -, *, /, %, **, //)
print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Modulus (%):", a % b)
print("Exponent (**):", a ** b)
print("Floor Division (//):", a // b)

# Comparison Operators (==, !=, >, <, >=, <=)
print("Equal (==):", a == b)
print("Not Equal (!=):", a != b)
print("Greater Than (>):", a > b)
print("Less Than (<):", a < b)
print("Greater or Equal (>=):", a >= b)
print("Less or Equal (<=):", a <= b)

# Logical Operators (and, or, not)
x = True
y = False
print("AND (and):", x and y)
print("OR (or):", x or y)
print("NOT (not):", not x)

# Assignment Operators (=, +=, -=, *=, /=)
c = 5
c += 3
print("c after += :", c)
c -= 2
print("c after -= :", c)

# Bitwise Operators (&, |, ^, ~)
print("Bitwise AND (&):", a & b)
print("Bitwise OR (|):", a | b)
print("Bitwise XOR (^):", a ^ b)
print("Bitwise NOT (~):", ~a)

# Membership Operators (in, not in)
my_list = [1, 2, 3]
print("2 in list:", 2 in my_list)
print("4 not in list:", 4 not in my_list)

# Identity Operators (is, is not)
m = [1, 2]
n = m
print("m is n:", m is n)
print("m is not n:", m is not n)