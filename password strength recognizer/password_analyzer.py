import re
import random
import string

common_passwords = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "welcome"
]

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for i in range(14))
    return password

def analyze_password(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        feedback.append("Use at least 8 characters")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters")

    # Number Check
    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add numbers")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        feedback.append("Add special characters")

    # Common Password Check
    if password.lower() not in common_passwords:
        score += 10
    else:
        feedback.append("Avoid common passwords")

    # Strength Level
    if score >= 80:
        strength = "Strong"
    elif score >= 50:
        strength = "Moderate"
    else:
        strength = "Weak"

    return score, strength, feedback

# Main Program
print("===== PASSWORD STRENGTH ANALYZER =====")

password = input("Enter your password: ")

score, strength, feedback = analyze_password(password)

print("\nPassword Strength:", strength)
print("Score:", score)

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)

# Generate Strong Password Suggestion
print("\nSuggested Strong Password:")
print(generate_strong_password())