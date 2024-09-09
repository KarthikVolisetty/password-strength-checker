# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 20:31:18 2024

@author: karth
"""

import re

def check_password_strength(password):
    # Checking length of password
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    
    # Checking for presence of lowercase, uppercase, numbers, and special characters
    if not re.search(r'[a-z]', password):
        return "Weak: Password should contain at least one lowercase letter."
    if not re.search(r'[A-Z]', password):
        return "Weak: Password should contain at least one uppercase letter."
    if not re.search(r'[0-9]', password):
        return "Weak: Password should contain at least one digit."
    if not re.search(r'[\W_]', password):
        return "Weak: Password should contain at least one special character."

    return "Strong password!"

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    print(check_password_strength(user_password))
