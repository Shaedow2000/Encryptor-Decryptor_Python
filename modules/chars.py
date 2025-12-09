import random
import string


def shuffle( key: str ) -> list:
    """
    A function that will shuffle the list of chars randomly depending on the key.
    """
    # this function will be shuffling the chars list in a way that the shuffle stays the same if the user enters the same key.
    # in another way, if u enter a key then excrypt a message, you will not be able to decrypt it.
    # so to decrypt the message you need the same key used to encrypt the message.
    chars: list[ str ] = list( string.printable + string.whitespace )

    lock = random.Random( key )

    lock.shuffle( chars )

    return chars
