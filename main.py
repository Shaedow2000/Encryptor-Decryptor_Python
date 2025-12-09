from cryptography.fernet import Fernet
from modules.encryptor import encrypt

def main() -> None:
    key = Fernet.generate_key()
    
    print( 'Enter the message that you want to encrypt:' )
    msg: str = input( '==> ' )

    encMsg = encrypt( msg, key )

    print( encMsg )

    




if __name__ == '__main__':
    main()
