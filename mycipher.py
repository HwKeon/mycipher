import sys
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determines if the character is uppercase
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += encrypted_char
    return encrypted_text
def main():
    # gets the amount to shift as command-line argument
    if len(sys.argv) != 2:
        print("Usage: python caesar_cipher.py 'shift'")
        sys.exit(1)
