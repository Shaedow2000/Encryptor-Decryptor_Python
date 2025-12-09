from cryptography.fernet import Fernet

def encrypt( msg, key ) -> str:
    fernet = Fernet( key )
    encrypted_msg: str = fernet.encrypt( msg.encode() )

    return encrypted_msg
