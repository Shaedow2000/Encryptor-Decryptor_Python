import random
import time
import string

ourchar = " " + string.ascii_letters + string.digits + string.punctuation  #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
char = list(ourchar) #Converts ourchar into a list so that we can shuffle it

random.shuffle(char) #Shuffles the list char so that the characters are in a random order






#User choice to continue or exit
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

#Encryption code
encryption = input("Enter a message to encrypt : ") #Takes user input for encryption
encrypted_text = " " #Empty string to store the encrypted text


for i in encryption: #Baisically sees how many words there are in the encrypt variable and coverts them one by one
    index = ourchar.index(i) #Finds the index of each character in the ourchar string
    encrypted_text += char[index] #Adds the corresponding character from the shuffled char list to the encrypted_text string

print(f"Original message : {encryption}") #Prints the original message
print(f"Encrypted message : {encrypted_text}") #Prints the encrypted message


#Decryption code


decryption = input("Enter a message to decrypt : ") #Takes user input for decryption
Dekrypted_text = "" #Empty string to store the decrypted text

for i in decryption: #Baisically sees how many words there are in the decrypt variable and coverts them one by one
    index = char.index(i) #Finds the index of each character in the char list
    Dekrypted_text += ourchar[index] #Adds the corresponding character from the ourchar string to the Dekrypted_text string

print(f"Encrypted message : {decryption}") #Prints the encrypted message
print(f"Decrypted message : {Dekrypted_text}") #Prints the decrypted message



#OUTPUT
# Enter a message to encrypt : Hello World!
# Original message : Hello World!
# Encrypted message : 9fGg}rYgqv
# Enter a message to decrypt : 9fGg}rYgqv   
# Encrypted message : 9fGg}rYgqv
# Decrypted message :  Hello World! 