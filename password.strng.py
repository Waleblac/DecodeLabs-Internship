import string
import sys
from getpass import getpass
from colorama import Fore, init

# Initialize colorama for colored terminal text
init(autoreset=True)


# 1. Function to load dataset into a set for fast O(1) lookups
def load_common_passwords(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            # Lowercase every entry so comparisons are case-insensitive
            return set(line.strip().lower() for line in f)
    except FileNotFoundError:
        print(Fore.RED + "[!] Password dataset file not found!")
        sys.exit(1)


# 2. Function to convert brute-force seconds into readable units
def convert_time(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif minutes < 60:
        return f"{minutes:.2f} minutes"
    elif hours < 24:
        return f"{hours:.2f} hours"
    elif days < 365:
        return f"{days:.2f} days"
    else:
        return f"{years:.2f} years"


def main():
    # --- MAIN EXECUTION ---
    # Load common password dataset
    common_passwords = load_common_passwords("xato-net-10-million-passwords-100.txt")

    # getpass hides input from the terminal — never echo a password in plaintext
    password = getpass(Fore.CYAN + "Enter your password: ")

    print("\n" + Fore.YELLOW + "Password Analysis")
    print("-" * 30)

    # Check common password list (case-insensitive)
    if password.lower() in common_passwords:
        print(Fore.RED + "[!] This password exists in a common password dataset!")
        print(Fore.RED + "Estimated Time to crack: Instantly!!")
        sys.exit(0)

    # Evaluation variables
    score = 0
    charset_size = 0

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Length check
    if len(password) >= 8:
        score += 1
        print(Fore.GREEN + "[+] Good password length")
    else:
        print(Fore.RED + "[-] Password is too short (minimum 8 characters)")

    # Character set checks
    if any(c.islower() for c in password):
        score += 1
        charset_size += len(lowercase)
        print(Fore.GREEN + "[+] Contains lowercase characters")

    if any(c.isupper() for c in password):
        score += 1
        charset_size += len(uppercase)
        print(Fore.GREEN + "[+] Contains Uppercase Characters")

    if any(c.isdigit() for c in password):
        score += 1
        charset_size += len(digits)
        print(Fore.GREEN + "[+] Contains numbers")

    if any(c in symbols for c in password):
        score += 1
        charset_size += len(symbols)
        print(Fore.GREEN + "[+] Contains special characters")

    # Fallback character set size if only unknown characters are entered
    if charset_size == 0:
        charset_size = 26

    # Calculate brute-force resistance
    combinations = charset_size ** len(password)
    guesses_per_second = 1_000_000_000  # 1 Billion guesses per second

    try:
        seconds = combinations / guesses_per_second
    except OverflowError:
        seconds = float("inf")

    # Output final analysis
    print("\n" + Fore.YELLOW + "Strength Result")
    print("-" * 30)

    # 5-point scale: length, lowercase, uppercase, digits, symbols
    if score <= 2:
        print(Fore.RED + "Weak Password")
    elif score in (3, 4):
        print(Fore.YELLOW + "Medium Password")
    else:
        print(Fore.GREEN + "Strong Password")

    if seconds == float("inf"):
        print(Fore.MAGENTA + "\nEstimated time to crack: effectively uncrackable by brute force")
    else:
        print(Fore.MAGENTA + f"\nEstimated time to crack: {convert_time(seconds)}")


if __name__ == "__main__":
    main()