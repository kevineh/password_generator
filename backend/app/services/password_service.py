"""
File: backend/app/services/password_service.py
Purpose: Password generation and validation logic
"""

import secrets
import string


class PasswordService:
    @staticmethod
    def generate_password(
        length: int, use_uppercase: bool, use_symbols: bool, use_numbers: bool
    ) -> str:
        # Define character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase if use_uppercase else ""
        symbols = string.punctuation if use_symbols else ""
        numbers = string.digits if use_numbers else ""

        # Combine all allowed characters
        all_chars = lowercase + uppercase + symbols + numbers

        if not all_chars:
            raise ValueError("At least one character set must be selected")

        # Ensure minimum requirements are met
        password = []
        if use_uppercase:
            password.append(secrets.choice(uppercase))
        if use_symbols:
            password.append(secrets.choice(symbols))
        if use_numbers:
            password.append(secrets.choice(numbers))

        # Fill remaining length with random characters
        remaining_length = length - len(password)
        password.extend(secrets.choice(all_chars) for _ in range(remaining_length))

        # Shuffle the password
        password_list = list(password)
        secrets.SystemRandom().shuffle(password_list)

        return "".join(password_list)
