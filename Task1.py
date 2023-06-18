import argparse

def main():
    parser = argparse.ArgumentParser(description='Program do przetwarzania argumentów.')
    parser.add_argument('arg1', type=int, help='Pierwszy argument (liczba całkowita)')
    parser.add_argument('arg2', type=str, help='Drugi argument (łańcuch znaków)')
    parser.add_argument('--optional', '-o', type=float, help='Opcjonalny argument (liczba zmiennoprzecinkowa)')

    args = parser.parse_args()

    # Wyświetlanie przekazanych argumentów
    print(f'arg1: {args.arg1}')
    print(f'arg2: {args.arg2}')

    if args.optional:
        print(f'optional: {args.optional}')
    else:
        print('optional: Niepodany')

if __name__ == '__main__':
    main()