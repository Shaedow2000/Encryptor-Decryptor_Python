import string
import random

#new and improved..

char = string.ascii_letters + string.digits + string.punctuation + " " #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
chars = list(char) #converts char into a list


def shuffle( chars: list[ str ] , key):
    """
    Shuffle list in a random way using a key.      <---
    """

    shuffled_chars: list[ str ] = chars[ : ]

    lock = random.Random( key )

    lock.shuffle( shuffled_chars )

    return shuffled_chars


def encrypt(encryption,  key) : #Encrypts the submitted text
    shuffled_chars: list[ str ] = shuffle( chars, key ) #<--- calls the shuffle function earlier defined
    msglist = list(encryption) #converts the encryption string into a list
    encrypted_msg_list = [] #creates an empty list to store the encrypted message

    for i in range(len(msglist)): #loops through the length of the message list
        index: int = chars.index(msglist[i]) #finds the index of each character in the original chars list
        encrypted_msg_list.append(shuffled_chars[index]) #adds the corresponding character from the shuffled chars list to the encrypted message list
    
    encryption = ''.join(encrypted_msg_list) #joins the encrypted message list into a string/word
    


    
    return encryption


def decrypt(decryption,key) : #Decrypts the submitted text
    shuffled_chars: list[ str ] = shuffle( chars, key ) #<--- calls the shuffle function earlier defined
    encrypted_msg_list = list(decryption) #converts the decryption string into a list
    msg_list = [] #creates an empty list to store the decrypted message
    for i in range(len(encrypted_msg_list)): #loops through the length of the encrypted message list
        index = shuffled_chars.index( encrypted_msg_list[ i ] ) #finds the index of each character in the shuffled chars list
        msg_list.append(char[index]) #adds the corresponding character from the original chars list to the decrypted message list
    decryption = ''.join(msg_list) #joins the decrypted message list into a string/word

        

    return decryption 


#MAIN PART OF THE PROGRAM :
while True:
    choice = input("Welcome to the Encryption-Decryption Program (press Q to exit) (E to start.) " \
            " (D to Decrypt.) and (H for help): ")
    if choice.lower() == 'q':
        break
    elif choice.lower() == 'e': 
        encryption = input("Enter text to encrypt: ")
        key = input("Enter encryption key: ")
        encryptions = encrypt(encryption, key)
        print(f"Encrypted text: {encryptions}")
    elif choice.lower() == 'd':
        decryption : str = input("Enter text to decrypt: ")
        key = input("Enter  decryption key: ")
        decryptions = decrypt(decryption, key)
        print(f"Decrypted text: {decryptions}")
    elif choice.lower() == 'h':
        print("This program allows you to encrypt and decrypt text using a custom key.")
        print("To encrypt text, choose 'E' and provide the text and a key.")
        print("To decrypt text, choose 'D' and provide the encrypted text and the same key used for encryption.")
        print("Press 'Q' to exit the program.")  
        print("Program provided by Monium and Sal")  
    else:
        print("Invalid choice. Please try again.")