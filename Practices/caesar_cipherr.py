# MR 2nd Caeser Cipher encoder and decoder

def encode(message, shift):
    """
    Encrypts a message using the Caesar cipher.
    
    Args:
        message (str): The plaintext message to encode.
        shift (int): The number of positions to shift each letter.
        
    Returns:
        str: The encoded message.
    """
    encoded_message = ""
    for char in message:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            new_position = (ord(char) - ord('a') + shift) % 26
            encoded_message += chr(new_position + ord('a'))
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            new_position = (ord(char) - ord('A') + shift) % 26
            encoded_message += chr(new_position + ord('A'))
        else:
            # Leave non-alphabetic characters unchanged
            encoded_message += char
    return encoded_message

def decode(message, shift):
    """
    Decrypts a message using the Caesar cipher.
    
    Args:
        message (str): The encoded message to decode.
        shift (int): The shift value used for encoding.
        
    Returns:
        str: The decoded message.
    """
    # Decoding is the same as encoding with a negative shift
    return encode(message, -shift)

def main():
    """
    Main function to run the Caesar cipher program.
    """
    while True:
        try:
            # Prompt user for operation choice
            choice = input("Choose operation (1 for encode, 2 for decode): ")
            if choice not in ['1', '2']:
                print("Invalid choice. Please enter 1 or 2.")
                continue

            # Prompt user for message and shift value
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))

            if choice == '1':
                # Encode the message
                result = encode(message, shift)
                print(f"\nEncoded message: {result}")
            else:
                # Decode the message
                result = decode(message, shift)
                print(f"\nDecoded message: {result}")
            
            # Ask if the user wants to continue
            continue_choice = input("\nDo you want to perform another operation? (yes/no): ").lower()
            if continue_choice != 'yes':
                break

        except ValueError:
            print("Invalid shift value. Please enter an integer.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
