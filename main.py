import os

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
            continue
        elif inp == 'q':
            print( '--> Exiting...' )
            break
        elif inp == '1':
            pass
        elif inp == '2':
            pass
        else: 
            print( f'!-> { inp } is an unknown command.' )
            continue


if __name__ == '__main__':
    main()
