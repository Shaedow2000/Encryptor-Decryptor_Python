from chars import shuffle

def encrypt( msg: str, key: str ) -> str:
    """
    Encrypts messages with a specific key entered by the user.
    """
    
    chars: list[ str ] = shuffle( key )[ 0 ]
    shuffled_chars: list[ str ] = shuffle( key )[ 1 ]

    list_msg: list[ str ] = list( msg )
   
    enc_msg_list: list[ str ] = []

    for i in range( list_msg.__len__() ):
        char_index: int = chars.index( list_msg[ i ] )
        enc_msg_list.append( shuffled_chars[ char_index ] )

    enc_msg: str = ''.join( enc_msg_list )

    return enc_msg

