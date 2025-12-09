import random
import string

ourchar = " " + string.ascii_letters + string.digits + string.punctuation 
char = list(ourchar)

random.shuffle(char)

#Encryption code 

encrypt = input("Enter a message to encrypt : ")
text = ' '


for i in encrypt: #Baisically sees how many words there are in choice and coverts them one by one
    index = ourchar.index(i)
    text += char[index]

print(f"Original message : {encrypt}")
print(f"Encrypted message : {text}")
#Decryption code

Dekrypt = input("Enter a message to decrypt : ")
Dekrypted_text = ""

for i in Dekrypt:
    index = char.index(i)
    Dekrypted_text += ourchar[index]

print(f"Encrypted message : {Dekrypt}")
print(f"Decrypted message : {Dekrypted_text}")