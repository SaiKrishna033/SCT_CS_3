# Password Strength Checker

## Overview

This project is a simple tool to assess the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. The tool helps users understand the security of their passwords and encourages the creation of stronger passwords.

## Features

- Checks password length
- Ensures presence of both uppercase and lowercase letters
- Checks for the inclusion of numbers
- Ensures the presence of special characters
- Provides a strength score and feedback

## Prerequisites

- Python 3.x

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/SaiKrishna033/SCT_CS_3.git
    cd password-strength-checker
    ```

2. **No additional libraries are required.**

## Usage

1. **Run the script:**

    ```sh
    python password_strength_checker.py
    ```

2. **Enter a password to check its strength:**

    ```plaintext
    Enter the password to check its strength: yourpassword
    ```

## Example

```plaintext
Enter the password to check its strength: P@ssw0rd123
Password strength: 5/5
Your password is very strong!
```

## Password Strength Criteria

- **Length:** At least 8 characters
- **Uppercase Letters:** At least one uppercase letter
- **Lowercase Letters:** At least one lowercase letter
- **Numbers:** At least one number
- **Special Characters:** At least one special character (e.g., @, #, $, etc.)
