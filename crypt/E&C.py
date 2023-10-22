import csv
import argon2
from cryptography.fernet import Fernet
from datetime import datetime

def generate_key():
    return Fernet.generate_key()

def encrypt(message, key):
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(message.encode())
    return ciphertext

def decrypt(ciphertext, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(ciphertext)
    return decrypted_message.decode()

def write_to_csv(content, filename='encryption_process.csv'):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, ""])  # New line with timestamp
        writer.writerow([content])

def main():
    key = generate_key()
    write_to_csv(f"Step 1: Generated Key: {key.decode()}")

    message = input("Enter a message: ")
    write_to_csv(f"Step 2: Entered Message: {message}")

    # Encrypt
    encrypted_message = encrypt(message, key)
    write_to_csv(f"Step 3: Encrypted Message: {encrypted_message.decode()}")

    # Decrypt
    decrypted_message = decrypt(encrypted_message, key)
    write_to_csv(f"Step 4: Decrypted Message: {decrypted_message}")
    print("\n")

if __name__ == "__main__":
    main()
    print("\n")
