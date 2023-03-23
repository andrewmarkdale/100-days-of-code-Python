"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
5

Project:
Password Generator

Purpose:
Generates a random password given a certain number of letters, numbers and symbols.

Example (albeit a bad one):
Input:
3 letters
2 symbols
2 numbers

Output:
2@Nb!3B

"""

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
total_char = nr_letters + nr_numbers + nr_symbols
pw_list = []

# Appending random letter character to our password list
for character in range(nr_letters):
    pw_list += random.choice(letters)

# Appending random symbol character to our password list
for character in range(nr_symbols):
    pw_list += random.choice(symbols)    

# Appending random number character to our password list
for character in range(nr_numbers):
    pw_list += random.choice(numbers)
    
# Shuffling our list to ensure password is more 'random'
random.shuffle(pw_list)

# List comprehension to return string
return_pw = "".join([x for x in pw_list])

print(return_pw)


