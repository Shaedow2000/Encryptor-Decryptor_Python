import os

from modules.encryptor import encrypt

def main() -> None:
    """
    main function
    """

    print( '1: encrypt | 2: decrypt | c: clear screen | q: quit' )
    while True:
        inp: str = input( '==> ' ).replace( ' ', '' ).lower()

        if inp == '':
            continue
        elif inp == 'c':
            os.system( 'cls' if os.name == 'nt' else 'clear' )
            print( '1: encrypt | 2: decrypt | c: clear screen | q: quit' )
            continue
        elif inp == 'q':
            print( '--> Exiting...' )
            break
        elif inp == '1':
            msg: str = input( '==> Message to encrypt: ' )
            print( '>> Please enter a secure key and save it to decrypt messages that use this key...' )
            key: str = input( '==> Key: ' )

            enc_msg: str = encrypt( msg, key )

            print( '\n!> Encrypted message:' )
            print( enc_msg )
        elif inp == '2':
            pass
        else: 
            print( f'!-> { inp } is an unknown command.' )
            continue


if __name__ == '__main__':
    main()
