def luhn_check(card_number: str) -> bool:
    """
    Validate a credit card number using the Luhn algorithm.

    Args:
        card_number (str): The credit card number as a string of digits.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Remove spaces and dashes
    card_number = card_number.replace(' ', '').replace('-', '')
    if not card_number.isdigit():
        return False

    digits = [int(d) for d in card_number]
    checksum = 0
    parity = len(digits) % 2

    for i, digit in enumerate(digits):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit

    return checksum % 10 == 0

if __name__ == "__main__":
    card = input("Enter credit card number: ")
    if luhn_check(card):
        print("Valid credit card number.")
    else:
        print("Invalid credit card number.")
