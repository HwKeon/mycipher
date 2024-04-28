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

    try:
        shift = int(sys.argv[1]) % 26
    except ValueError:
        print("Shift must be an integer")
        sys.exit(1)

    # Read the message from stdin
    message = input().upper()

    # Encode the message using Caesar cipher
    encoded_message = caesar_cipher(message, shift)

    # Print the final encoded message in 10 blocks of five letters per line
    bsize = 5
    bper_line = 10
    for i in range(0, len(encoded_message), bsize * bper_line):
        line = encoded_message[i:i + bsize * bper_line]
        for j in range(0, len(line), bsize):
            print(line[j:j + bsize], end=" ")
        print()

if __name__ == "__main__":
    main()

