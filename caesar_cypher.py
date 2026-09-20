#!/usr/bin/env python3
"""
Project 2: Basic Encryption & Decryption
------------------------------------------
Implements a Caesar cipher: shifts each letter of the alphabet by a fixed
number of positions ('the shift' / 'the key'). Encryption shifts forward,
decryption shifts backward by the same amount.

"""

import argparse
import string


def caesar_shift(text: str, shift: int, decrypt: bool = False) -> str:
   
    if decrypt:
        shift = -shift

    result_chars = []
    for char in text:
        if char in string.ascii_uppercase:
            # ord('A') = 65. Subtracting it maps A-Z to 0-25 so we can do
            # modular arithmetic, then we add it back to return to ASCII.
            new_index = (ord(char) - ord('A') + shift) % 26
            result_chars.append(chr(new_index + ord('A')))
        elif char in string.ascii_lowercase:
            new_index = (ord(char) - ord('a') + shift) % 26
            result_chars.append(chr(new_index + ord('a')))
        else:
            # Leave digits, punctuation, spaces untouched.
            result_chars.append(char)

    return "".join(result_chars)


def encrypt(plaintext: str, shift: int) -> str:
    return caesar_shift(plaintext, shift, decrypt=False)


def decrypt(ciphertext: str, shift: int) -> str:
    return caesar_shift(ciphertext, shift, decrypt=True)


def run_interactive():
    """Simple guided mode when no CLI flags are given."""
    print("=== Basic Encryption & Decryption (Caesar Cipher) ===\n")
    text = input("Enter text: ")
    while True:
        try:
            shift = int(input("Enter shift key (integer, e.g. 3): "))
            break
        except ValueError:
            print("Please enter a whole number.")

    enc = encrypt(text, shift)
    dec = decrypt(enc, shift)

    print("\n--- Results ---")
    print(f"Original text : {text}")
    print(f"Shift key     : {shift}")
    print(f"Encrypted     : {enc}")
    print(f"Decrypted     : {dec}")
    print(f"Round-trip OK : {dec == text}")


def main():
    parser = argparse.ArgumentParser(
        description="Basic Caesar cipher encryption/decryption tool."
    )
    parser.add_argument("-t", "--text", help="Text to encrypt or decrypt")
    parser.add_argument("-s", "--shift", type=int, help="Shift key (integer)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the text")
    group.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the text")

    args = parser.parse_args()

    # If no text/shift given, fall back to interactive mode.
    if args.text is None or args.shift is None:
        run_interactive()
        return

    if args.decrypt:
        output = decrypt(args.text, args.shift)
        action = "Decrypted"
    else:
        # Default to encrypt if neither flag (or -e) was given.
        output = encrypt(args.text, args.shift)
        action = "Encrypted"

    print(f"Original : {args.text}")
    print(f"Shift    : {args.shift}")
    print(f"{action}: {output}")


if __name__ == "__main__":
    main()