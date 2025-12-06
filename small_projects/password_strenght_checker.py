"""
Password Strength Checker
Author: Sithum-Devops
Checks:
        - Length >= 8 characters
        - Uppercase letters
        - Lowercase letters
        - Digits
        - Special characters
"""

import string

def check_strength(password):
    """Check the strength of a password."""
    score = 0
    messages = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        messages.append("Password should be at least 8 characters.")

    # Check for uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        messages.append("Add at least one uppercase letter.")

    # Check for lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        messages.append("Add at least one lowercase letter.")

    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        messages.append("Add at least one number.")

    # Check for special characters
    special_chars = string.punctuation
    if any(c in special_chars for c in password):
        score += 1
    else:
        messages.append("Add at least one special character (!@#$ etc).")

    # Determine strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, messages


# ---------------------------
# Run the checker directly
# ---------------------------
print("Welcome to the Password Strength Checker!")
password = input("Enter a password to check: ").strip()
strength, messages = check_strength(password)

print(f"\nPassword Strength: {strength}")
if messages:
    print("Suggestions to improve your password:")
    for msg in messages:
        print(" -", msg)
else:
    print("Your password is strong! Well done.")
    print("*"*40)
    print("\nLearn with Sithum")
