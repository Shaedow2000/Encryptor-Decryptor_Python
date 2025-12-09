from modules.chars import shuffle

def decrypt( enc_msg: str, key: str ) -> str:
    """
    decrypt a message using a specific key.
    """

    chars: list[ str ] = shuffle( key )[ 0 ]
    shuffled_chars: list[ str ] = shuffle( key )[ 1 ]

    list_msg: list[ str ] = list( enc_msg )
   
    msg_list: list[ str ] = []

    for i in range( list_msg.__len__() ):
        char_index: int = shuffled_chars.index( list_msg[ i ] )
        msg_list.append( chars[ char_index ] )

    msg: str = ''.join( msg_list )

    return msg
