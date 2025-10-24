# MR 2nd Caeser Cipher encoder and decoder
# first we will make a variable from a user input that they can choose to encode or decode
print("Welcome to the Ceaser Cipher encoder and decoder!")
action = input("Do you want to encode or decode a message: ")
caeser_encode = input("What is the message you want to encode: ")
def caeser_encode(message, shift):
    print("How many times would you like me to shift your message? ")
encoded_message = 
for char in message:
        if 'a' <= char <= 'z':
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif 'A" <= char <= 'z' :
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('A'))
        else:
             shifted_char = char
        encoded_message += shifted_char
    return encoded_message



key
def decode():
    print(decode)

# Then we will ask for the message that needs to be processed
# Then we will ask for the shift value which has to be an integer
# Then we will display the result of the encoded or decoded message

