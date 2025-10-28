# MR 2nd Caeser Cipher encoder and decoder
# first we will welcome the user using a print statement
print("Welcome to the Ceaser Cipher encoder and decoder!")
# then we will make a funcitons so we can find out the message and how many times the user wants to shift it
def encode(message, shift):
# we will ask for the mesage they want to encode
    encoded_message = ""
# Then we will ask how many times they want to shift it and then we will shift it
    for char in message:
        if 'a' <= char <= 'z':
            # shift the message
            new_position = (ord(char) - ord('a') + shift) % 26
            encoded_message += chr(new_position + ord('a'))
        elif 'A' <= char <= 'Z':
            # shift the upper case letters
            new_position = (ord(char) - ord('A') + shift) % 26
            encoded_message += chr(new_position + ord('A'))
        else:
            #  we will not change anything else that is not a letter
            encoded_message += char
    return encoded_message
def decode(message, shift):
# we will make a funciton to decode the message the user gives us
    # Decoding is the same as encoding with a negative shift
    return encode(message, -shift)

def main():

    while True:
        try:
            # we will then make a loop so the user can decode and encode as many messages as they want
            choice = input("Choose operation (1 for encode, 2 for decode): ")
            if choice not in ['1', '2']:
                print("Invalid choice. Please enter 1 or 2.")
                continue

            # we will repeat the process of asking all the questions
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
# this we will use a value error to check if the use inputted something valid
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()



