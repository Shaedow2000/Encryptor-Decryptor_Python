import string
import random

# new and improved but with constructors 

char = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(char)  # converts char into a list


class EDP: # Encryption Decryption Program (ik its sus lol)
    def __init__(self, key): # initializes the key
        self.key = key # stores the key

    def shuffle(self, chars): 
        """
        Shuffle list in a random way using a key.
        """
        shuffled_chars = list(chars)
        lock = random.Random(self.key)
        lock.shuffle(shuffled_chars)
        return shuffled_chars

    def encrypt(self, encryption):  # Encrypts the submitted text
        shuffled_chars = self.shuffle(chars) # shuffles the chars using the key
        msglist = list(encryption) # converts the encryption into a list
        encrypted_msg_list = [] # empty list to store the encrypted message

        for i in range(len(msglist)): # iterates through the message list
            index = chars.index(msglist[i]) # finds the index of the character in the original chars list
            encrypted_msg_list.append(shuffled_chars[index]) # adds the corresponding character from the shuffled list

        encryption = ''.join(encrypted_msg_list) # joins the list into a string
        return encryption # returns the encrypted message

    def decrypt(self, decryption):  # Decrypts the submitted text
        shuffled_chars = self.shuffle(chars) # shuffles the chars using the key
        encrypted_msg_list = list(decryption) # converts the decryption into a list
        msg_list = [] # empty list to store the decrypted message

        for i in range(len(encrypted_msg_list)): # iterates through the encrypted message list
            index = shuffled_chars.index(encrypted_msg_list[i]) # finds the index of the character in the shuffled chars list
            msg_list.append(char[index]) # adds the corresponding character from the original chars list

        decryption = ''.join(msg_list) # joins the list into a string
        return decryption # returns the decrypted message


# MAIN PART OF THE PROGRAM :
def main():
    while True:
        choice = input(
            "Welcome to the Encryption-Decryption Program (press Q to exit) "
            "(E to start.) (D to Decrypt.) and (H for help): "
        )

        if choice.lower() == 'q':
            break

        elif choice.lower() == 'e':
            encryption = input("Enter text to encrypt: ")
            key = input("Enter encryption key: ")
            encryptions = EDP(key).encrypt(encryption)
            print(f"Encrypted text: {encryptions}")

        elif choice.lower() == 'd':
            decryption = input("Enter text to decrypt: ")
            key = input("Enter  decryption key: ")
            decryptions = EDP(key).decrypt(decryption)
            print(f"Decrypted text: {decryptions}")

        elif choice.lower() == 'h':
            print("This program allows you to encrypt and decrypt text using a custom key.")
            print("To encrypt text, choose 'E' and provide the text and a key.")
            print("To decrypt text, choose 'D' and provide the encrypted text and the same key used for encryption.")
            print("Press 'Q' to exit the program.")
            print("Program provided by Monium and Sal")

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
