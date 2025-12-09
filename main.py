import random
import time
import string

ourchar = " " + string.ascii_letters + string.digits + string.punctuation 
char = list(ourchar)

random.shuffle(char)

print(char)

#Encryption code 


urchoice = input("Welcome to the decryption/encryption program! Press Q to exit and C to continue: ")

while True:
    if urchoice.upper() == "Q":
        print("Exiting the program. Goodbye!")
        time.sleep(1)
        break
    elif urchoice.upper() == "C":
        print("Continuing to the encryption/decryption process.")
        time.sleep(1)
        break
    else:
        urchoice = input("Invalid input. Please press Q to exit and C to continue: ")


encryption = input("Enter a message to encrypt : ")
encrypted_text = " "


for i in encryption: #Baisically sees how many words there are in the encrypt variable and coverts them one by one
    index = ourchar.index(i)
    encrypted_text += char[index]

print(f"Original message : {encryption}")
print(f"Encrypted message : {encrypted_text}")
#Decryption code


decryption = input("Enter a message to decrypt : ")
Dekrypted_text = ""

for i in decryption:
    index = char.index(i)
    Dekrypted_text += ourchar[index]

print(f"Encrypted message : {decryption}")
print(f"Decrypted message : {Dekrypted_text}")



#OUTPUT
# Enter a message to encrypt : Hello World!
# Original message : Hello World!
# Encrypted message : 9fGg}rYgqv
# Enter a message to decrypt : 9fGg}rYgqv   
# Encrypted message : 9fGg}rYgqv
# Decrypted message :  Hello World! 