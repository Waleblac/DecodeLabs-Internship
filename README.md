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
