import random, string, sys, os

def clear() -> None:
    os.system( 'cls' if os.name == 'nt' else 'clear' )

class Cryptographic:
    chars: list[ str ] = list( string.ascii_letters + string.digits + string.punctuation + ' ' )

    def shuffle( self, key: str ) -> list[ str ]:
        lock = random.Random( key )
        shuffled_chars: list[ str ] = self.chars[ : ]
        lock.shuffle( shuffled_chars )

        return shuffled_chars

    def encrypt( self, msg: str, key: str ) -> str:
        msg_list: list[ str ] = list( msg )
        shuffled_chars: list[ str ] = self.shuffle( key )

        enc_msg_list: list[ str ] = []

        for i in range( len( msg_list ) ):
            char_index: int = self.chars.index( msg_list[ i ] )
            enc_msg_list.append( shuffled_chars[ char_index ] )

        enc_msg: str = ''.join( enc_msg_list )

        return enc_msg

    def decrypt( self, enc_msg: str, key: str ) -> str:
        enc_msg_list: list[ str ] = list( enc_msg )
        shuffled_chars: list[ str ] = self.shuffle( key )

        msg_list: list[ str ] = []

        for i in range( len( enc_msg_list ) ):
            char_index: int = shuffled_chars.index( enc_msg_list[ i ] )
            msg_list.append( self.chars[ char_index ] )

        msg: str = ''.join( msg_list )

        return msg

def main() -> None:
    menu: str = '\t=> Entrer une command:  e: encrypt | d: decrypt | c: clear screen | q: quit.'
    print( menu )

    cryptographic: Cryptographic = Cryptographic()

    while True:
        choice: str = input( '--> Command: ' ).replace( ' ', '' ).lower()

        if choice == 'e':
            msg: str = input( '|> Enter message: ' )
            key: str = input( '|> Enter secure key: ' )

            print( cryptographic.encrypt( msg, key ) )
        elif choice == 'd':
            enc_msg: str = input( '|> Enter encrypted message: ' )
            key: str = input( '|> Enter the key used to encrypt: ' )

            print( cryptographic.decrypt( enc_msg, key ) )
        elif choice == 'c':
            clear()
            print( menu )
        elif choice == 'q':
            print( '--> Quiting program...' )
            sys.exit( 1 )
        else:
            print( f'!> Unknown command [ { choice } ].' )
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n-->Quiting program...' )
        sys.exit( 1 )
