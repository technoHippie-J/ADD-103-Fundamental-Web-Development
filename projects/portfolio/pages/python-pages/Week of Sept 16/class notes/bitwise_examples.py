# Bitwise AND (&)
# The & operator compares each bit of the first operand with the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, it's set to 0.

a = 9   # 1001 in binary
b = 5   # 0101 in binary
result = a & b  # 0001 in binary which is 1 in decimal
print(result)

# result = 1

# Bitwise OR (|)
# The | operator compares each bit of the first operand with the corresponding bit of the second operand. If either of the bits is 1, it gives 1, otherwise it gives 0.

a = 9   # 1001 in binary
b = 5   # 0101 in binary
result = a | b  # 1101 in binary which is 13 in decimal
print(result)

# result = 13

# Bitwise NOT (~)
# The ~ operator is a unary operator and works by inverting all the bits of the operand. In Python, ~x is defined as -(x+1).

a = 9   # 1001 in binary
result = ~a  # -(1001 + 1) in binary, which is -10 in decimal
print(result)

# result = -10

# Bitwise XOR (^)
# The ^ operator compares each bit of the first operand with the corresponding bit of the second operand. If the bits are different, it gives 1, and if they're the same, it gives 0.

a = 9   # 1001 in binary
b = 5   # 0101 in binary
result = a ^ b  # 1100 in binary which is 12 in decimal
print(result)

# result = 12

12 in binary = 1100
10 in binary = 1010
Applying AND = 1000

15 in binary = 1111
6 in binary = 0110
Applying AND = 0110 = 6
