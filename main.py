import random
import string
import sys
import os

chars: list[ str ] = list( string.ascii_letters + string.digits + string.punctuation + ' ' )
commands_msg: str = '\tq: quit | 1: encrypt | 2: decrypt | c: clear screen'

def shuffle( chars: list[ str ], key: str ) -> list[ str ]:
    """
    Shuffle list in a random way using a key.
    """

    shuffled_chars: list[ str ] = chars[ : ]

    lock = random.Random( key )

    lock.shuffle( shuffled_chars )

    return shuffled_chars

def encrypt( msg: str, key: str ) -> str:
    """
    Encrypt a message using a key.
    """
    
    shuffled_chars: list[ str ] = shuffle( chars, key )

    list_msg: list[ str ] = list( msg )
    enc_msg_list: list[ str ] = []

    for i in range( list_msg.__len__() ):
        char_index: int = chars.index( list_msg[ i ] )
        enc_msg_list.append( shuffled_chars[ char_index ] )

    enc_msg: str = ''.join( enc_msg_list )

    return enc_msg


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
        elif inp == '':
            continue
        elif inp == '1':
            msg: str = input( '-> Enter message to encrypt: ' )
            key: str = input( '-> Enter a secure key: ' )
            enc: str = encrypt( msg, key )

            print( f'==> Encrypted message: \n{ enc }' )
        elif inp == '2':
            decrypt( '', '' )
        else:
            print( f'!> Unknown command { inp }.' )
            continue


if __name__ == '__main__':
    main()
