import re

def password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[\W_]', password))  # \W matches any non-word character, which includes special characters

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    
    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak"
    }
    
    print(f"Password: {password}")
    print(f"Length Criteria: {'Passed' if length_criteria else 'Failed'}")
    print(f"Uppercase Criteria: {'Passed' if uppercase_criteria else 'Failed'}")
    print(f"Lowercase Criteria: {'Passed' if lowercase_criteria else 'Failed'}")
    print(f"Number Criteria: {'Passed' if number_criteria else 'Failed'}")
    print(f"Special Character Criteria: {'Passed' if special_criteria else 'Failed'}")
    
    return strength[score]

def main():
    password = input("Enter the password to assess: ")
    strength = password_strength(password)
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
