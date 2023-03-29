#!/usr/bin/env python3

# AOT13
# source_message = input("What is the message to encrypt/decrypt? >> ")
# # Convert message to lower-case for simplicity
# source_message = source_message.lower()
# final_message = ""

# # Loop through each letter in the source message
# for letter in source_message:
#     # Convert the letter to the ASCII equivalent
#     ascii_num = ord(letter)
#     # Check to see if an alphabetic (a-z) character, if not, skip
#     if ascii_num >= 97 and ascii_num <= 122:
#         # Add 13 to ascii_num to "shift" it by 13
#         new_ascii = ascii_num + 13
#         # Confirm new character will be alphabetic 
#         if new_ascii > 122:
#             # If not, wrap around
#             new_ascii = new_ascii - 26
#         final_message = final_message + chr(new_ascii)
#     else:
#         final_message = final_message + chr(ascii_num)

# # Print converted message
# print("Message has been converted:")
# print(final_message)

# Base64
import base64

def encode_data(plain_text):
    # Convert plain_text string to bytes
    plain_text = plain_text.encode()
    # Encode the plain_text
    cipher_text = base64.b64encode(plain_text)
    # Convert the encoded bytes back to string
    cipher_text = cipher_text.decode()
    return cipher_text

def decode_data(cipher_text):
    # Decode the cipher_text
    plain_text = base64.b64decode(cipher_text)
    # Convert the decoded bytes to string
    plain_text = plain_text.decode()
    return plain_text

# Prompt the user for method and message
method = input("Do you wish to Encode or Decode (e/d)? >> ").lower()
message = input("What is the message? >> ")

# Using first letter in variable, call the encode or decode function
if method[0] == "e":
    print(encode_data(message))
elif method[0] == "d":
    print(decode_data(message))
else:
    # if method wasnt "e" or "d", print error message and quit
    print("Wrong method selected. Choose Encode or Decode")
