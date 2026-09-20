# DecodeLabs-Internship
# Password Strength Checker

A command-line tool that analyzes a password's strength and estimates how long
it would take to crack via brute force. Built as Project 1 (Password Strength
Checker) for the DecodeLabs Cyber Security Industrial Training Kit.

## What it does

- Checks the password against a list of known common/leaked passwords
- Evaluates length and character diversity (lowercase, uppercase, digits, symbols)
- Calculates the total keyspace (`charset_size ^ password_length`) and estimates
  brute-force crack time assuming 1 billion guesses/second
- Classifies the result as **Weak**, **Medium**, or **Strong**

## Why it works this way

Password strength isn't just "did you use a symbol" — it's about entropy: how
large the search space an attacker has to try is. This tool scores based on
which character sets are present (which determines the keyspace size) and
password length (which the keyspace is raised to the power of), then converts
that into a human-readable crack-time estimate. It also checks against a
common-password dataset first, since a long password that's still a known
leaked password offers effectively zero real-world protection regardless of
its theoretical entropy.

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Provide a common-password dataset as a plain text file, one password per
   line, named `xato-net-10-million-passwords-100.txt` in the same directory
   (or update the filename in the script). A good public source is
   [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

   > This dataset is not included in this repo — grab it yourself from a
   > public source and drop it in the project folder.

3. Run it:
   ```bash
   python password_strength_checker.py
   ```

## Example

```
Enter your password:

Password Analysis
------------------------------
[+] Good password length
[+] Contains lowercase characters
[+] Contains Uppercase Characters
[+] Contains numbers
[+] Contains special characters

Strength Result
------------------------------
Strong Password

Estimated time to crack: 214.67 years
```

## Notes

- Passwords are entered via `getpass`, so they are never echoed to the terminal.
- The crack-time estimate is a simplified model (assumes pure brute force at a
  fixed guess rate) — it doesn't account for smarter attacks like dictionary
  or rule-based guessing.

## Skills demonstrated

String handling, conditional logic, basic entropy/security math, and secure
input handling in Python.

# Project 2: Basic Encryption & Decryption (Caesar Cipher)

A command-line tool that encrypts and decrypts text using a Caesar cipher, built as part of the DecodeLabs Cyber Security Industrial Training Kit (Batch 2026).

## Goal

Implement a simple, reversible encryption and decryption technique, demonstrating the fundamentals of symmetric-key cryptography: the same key (shift value) both encrypts and decrypts the message.

## How It Works

The Caesar cipher shifts each letter of a message a fixed number of positions through the alphabet. For example, with a shift of 3: `A → D`, `B → E`, ..., wrapping back around at the end of the alphabet (`Z → C`).

**The core transformation** (applied per character):
```
new_index = (ord(char) - base + shift) % 26
```
- `ord(char)` converts the letter to its ASCII value (e.g. `ord('A')` = 65)
- Subtracting the base (`ord('A')` = 65 or `ord('a')` = 97) re-maps the letter into 0–25 space
- Adding the shift moves the letter forward (encryption) or backward, using a negative shift (decryption)
- `% 26` wraps the result around so it stays within the 26-letter alphabet
- `chr(new_index + base)` converts the number back into a letter

Decryption is the same operation as encryption, just with the shift negated — this is what makes it symmetric: one key locks and unlocks the message.

## Features

- **Encrypts** user-supplied text using the Caesar cipher
- **Decrypts** ciphertext back to the original message
- **Displays both** the encrypted and decrypted output, plus a round-trip check confirming `decrypt(encrypt(x)) == x`
- **Preserves case** — uppercase and lowercase letters are shifted independently, so casing in the original text is retained
- **Preserves non-letters** — spaces, punctuation, and digits pass through unchanged
- **Two modes**: command-line flags for scripting, or an interactive prompt for guided use

## Requirements

- Python 3.x (no external libraries — only the standard library `argparse` and `string` modules)

## Usage

**Command-line mode:**
```bash
# Encrypt
python3 caesar_cipher.py -e -t "Attack at dawn" -s 3
# Output: Dwwdfn dw gdzq

# Decrypt
python3 caesar_cipher.py -d -t "Dwwdfn dw gdzq" -s 3
# Output: Attack at dawn
```

**Interactive mode** (no flags — prompts for text and shift):
```bash
python3 caesar_cipher.py
```

**On Kali Linux / any Unix system**, you can also make it directly executable:
```bash
chmod +x caesar_cipher.py
./caesar_cipher.py -e -t "Attack at dawn" -s 3
```

## Example Output

```
Original : Attack at dawn
Shift    : 3
Encrypted: Dwwdfn dw gdzq
```

## Security Note

The Caesar cipher is used here for learning purposes, not real-world data protection. It has only 25 possible non-trivial shifts, making it trivially breakable by brute force, and it preserves the letter-frequency pattern of the original language, making it vulnerable to frequency analysis. Real-world systems (e.g. AES-256) use vastly larger keyspaces and more complex transformations to resist these attacks — this project is a first step toward understanding that larger picture, not a production-grade cipher.

## Key Skills Demonstrated

- Encryption/decryption concepts (symmetric-key logic)
- ASCII-based character manipulation (`ord()`, `chr()`)
- Modular arithmetic for cyclic wraparound
- Command-line interface design with `argparse`
- Input validation and self-verification (round-trip testing)
