"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
8

Project:
Caesar Cipher

Purpose:
Encrypt/decrypt messages using Caesar Cipher

"""

# Given starter code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


# My code
 
# Encrypting text
def encrypt(plain_text, shift_num):
    encrypted = ""
    len_of_alphabet = len(alphabet)
    for letter in plain_text: # For each letter in given word
        index = alphabet.index(letter) # Finding the index of given letter in alphabet list
        if (index + shift_num) >= len_of_alphabet: # Ensuring no out of index errors occur
            over_shift = (index + shift_num) - len_of_alphabet
            encrypted += alphabet[over_shift]
        else:
            encrypted += alphabet[index + shift_num]
    return encrypted

# Decrypting function
def decrypt(encrypted_text, shift_num):
    decrypted = ""
    for letter in encrypted_text:
        index = alphabet.index(letter)
        decrypted += alphabet[index - shift_num]
    return decrypted

# She has us turn both functions into a single one
def caesar_cipher(starter_text, shift_num, direction):
    return_text = ""
    if direction == "decode":
        shift_num *= -1
    for letter in starter_text:
        index = alphabet.index(letter)
        if index + shift_num > len(alphabet):
            return_text += alphabet[(index + shift_num) - len(alphabet)]
        else:
            return_text += alphabet[index + shift_num]
    return return_text

"""
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == "encode":
            print(f"The encoded text is: {encrypt(text, shift)}")
            cont = input("Would you like to continue? Y/N: ")
            if cont.lower() == "n":
                break;
        elif direction == "decode":
            print(f"The decoded text is: {decrypt(text, shift)}")
            cont = input("Would you like to continue? Y/N: ")
            if cont.lower() == "n":
                break;
    else: 
        print("Please enter a valid option.\n")
"""

# Improved single function version

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    
    if direction != "encode" and direction != "decode":
        print("Please enter a valid option")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        new_text = caesar_cipher(text, shift, direction)
        print(f"The {direction}d text is: {new_text}")
        cont = input("Would you like to continue? Y/N: ")
        if cont.lower() == "n":
            break
#print(encrypt(text, shift))
#print(decrypt(encrypt(text, shift), shift)) 