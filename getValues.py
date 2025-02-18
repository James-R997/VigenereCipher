#!/bin/python3

shifted = input("Enter the shifted letter: ")
original = input("Enter the original: ")


# Convert both letters to 0-based indices
shiftedn = ord(shifted.upper()) - ord("A")
originaln = ord(original.upper()) - ord("A")

# Calculate the shift, accounting for the circular alphabet
shift = (shiftedn - originaln) % 26
shiftChar = chr(shift + ord("A"))


print(f"{shifted}: {shiftedn}\n{original}: {originaln}")
print(f"\nThe shift is {shift}")
print(f"{shiftChar}")
