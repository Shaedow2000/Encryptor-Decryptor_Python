import random
import string
import sys
import os

chars: list[ str ] = list( string.ascii_letters + string.digits + ' ' )
commands_msg: str = '\tq: quit | 1: encrypt | 2: decrypt | c: clear screen'

def shuffle( chars: list[ str ], key: str ) -> list[ str ]:
    """
    Shuffle list in a random way using a key.
    """

    rand = random.Random( key )

    rand.shuffle( chars )

    return chars

def encrypt( msg: str, key: str ) -> str:
    """
    Encrypt a message using a key.
    """
    
    pass

def decrypt( enc_msg: str, key: str ) -> str:
    """
    Decrypt a message using a specific key.
    """

    pass

def main() -> None:
    """
    Main function.
    """
    print( commands_msg )

    while True:
        inp: str = input( '=> ' ).replace( ' ', '' ).lower()

        if inp == 'q':
            print( '--> Exiting...' )
            break
        elif inp == 'c':
            os.system( 'cls' if os.name == 'nt' else 'clear' )
            print( commands_msg )
            continue
        elif inp == '1':
            encrypt( '', '' )
        elif inp == '2':
            decrypt( '', '' )
        else:
            print( f'!> Unknown command { inp }.' )
            continue


if __name__ == '__main__':
    main()
