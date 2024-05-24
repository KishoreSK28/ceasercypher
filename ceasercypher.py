def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Loop through each character in the text
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Shift character and wrap around alphabet if necessary
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            # Shift character and wrap around alphabet if necessary
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If character is not a letter, leave it unchanged
            result += char

    return result

# Example usage:
plaintext = input("enter the plain text:")
shift = int(input("enter the shift value:"))

# Encrypt the plaintext
encrypted_text = caesar_cipher(plaintext, shift, mode='encrypt')
print(f"Encrypted: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
print(f"Decrypted: {decrypted_text}")
