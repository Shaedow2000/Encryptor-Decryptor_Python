from cryptography.fernet import Fernet

def main() -> None:
    key: str = Fernet.generate_key()
    fernet = Fernet( key )




if __name__ == '__main__':
    main()
