# ==============================================================================
# ACU CSE 101: Week 01 Guided Workshop - The Way of the Program & Variables
# Think Python: Chapters 1 & 2
#
# INSTRUCTOR & STUDENT IN-CLASS WORKSHOP:
# Welcome to Python! Do not worry about solving this alone.
# You will write the code for each part below together with your instructor / TA
# during our live lecture & lab session.
#
# Follow along with your instructor as we explore:
# 1. Using input() to read strings from the user
# 2. Converting user input with int() and float()
# 3. Cleaning user input with .strip()
# 4. Floating-point comparison pitfalls (math.isclose)
# 5. Exact decimal arithmetic for financial calculations (Decimal)
# 6. Multiple assignment & variable swapping (a, b = b, a)
# 7. Chained assignment (x = y = 50) and independent re-binding
# 8. String operations (+ concatenation, * repetition, len, methods)
# 9. String formatting for print() (f-string precision, alignment, sep & end)
# ==============================================================================

import math  # noqa: F401
from decimal import Decimal  # noqa: F401

# ------------------------------------------------------------------------------
# Part 1: Reading Text with input()
# input() pauses execution and waits for the user to type something.
# It ALWAYS returns the entered value as a string (str).
#
# In-Class Goal:
# 1. Ask for the user's name: user_name = input("Enter your name: ")
# 2. Greet the user: print(f"Hello, {user_name}! Welcome to CSE 101.")
# ------------------------------------------------------------------------------
# TODO: Write Part 1 together in class below:


# ------------------------------------------------------------------------------
# Part 2: Integer Input & Type Conversion - int()
# If we need a whole number for arithmetic, convert the string using int().
#
# In-Class Goal:
# 1. Ask user for birth year: birth_year = int(input("Enter your birth year: "))
# 2. Calculate age: age = 2026 - birth_year
# 3. Print: print(f"You will turn {age} years old in 2026.")
# ------------------------------------------------------------------------------
# TODO: Write Part 2 together in class below:


# ------------------------------------------------------------------------------
# Part 3: Float Input & Type Conversion - float()
# If the number has decimal places, convert the string using float().
#
# In-Class Goal:
# 1. Ask user for Celsius: celsius = float(input("Enter temperature in Celsius: "))
# 2. Convert to Fahrenheit: fahrenheit = (celsius * 9 / 5) + 32
# 3. Print: print("Fahrenheit:", fahrenheit)
# ------------------------------------------------------------------------------
radius = 5.0
volume = (4 / 3) * math.pi * (radius**3)
print("Sphere volume:", volume)

print("Hello AH! (Mardin Nasouti)")
