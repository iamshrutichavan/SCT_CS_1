def caesar_cipher(text, shift, direction):
    result = ""
    
    if direction == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char

    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    
    while True:
        direction = input("Would you like to encrypt or decrypt the text? (Enter 'encrypt' or 'decrypt'): ").lower()
        if direction in ["encrypt", "decrypt"]:
            break
        else:
            print("Invalid input. Please enter 'encrypt' or 'decrypt'.")
    
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (e.g., 3): "))
    
    result = caesar_cipher(text, shift, direction)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
