import random
import string

print("Smart password generator")

#take length from the user 
length = int(input("Enter the length of the password:"))
 
 #characters define
letters =string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

#password generation
password = ""

for i in range(length):
    password +=random.choice(all_characters)

print("Generated password:", password)