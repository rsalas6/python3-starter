"""
This module provides a simple calculator to add or subtract two numbers
using command line arguments.
"""

import argparse


def suma(a: int, b: int) -> int:
    """
    Add two numbers.

    Parameters
    ----------
    a : int
        The first number.
    b : int
        The second number.

    Returns
    -------
    int
        The sum of a and b.
    """
    return a + b


def resta(a: int, b: int) -> int:
    """
    Subtract two numbers.

    Parameters
    ----------
    a : int
        The first number.
    b : int
        The second number.

    Returns
    -------
    int
        The result of subtracting b from a.
    """
    return a - b


def main() -> None:
    """
    Parse command line arguments and execute the corresponding operation.

    This function parses the command line arguments to determine
    whether to add or subtract two numbers and then performs the
    specified operation.

    Returns
    -------
    None
        This function does not return any value.
    """
    parser = argparse.ArgumentParser(
        description='Simple calculator to add or subtract two numbers.'
    )

    subparsers = parser.add_subparsers(dest='command', help='Command to execute')

    # Subparser for the 'suma' command
    parser_suma = subparsers.add_parser('suma', help='Add two numbers')
    parser_suma.add_argument('a', type=int, help='The first number')
    parser_suma.add_argument('b', type=int, help='The second number')

    # Subparser for the 'resta' command
    parser_resta = subparsers.add_parser('resta', help='Subtract two numbers')
    parser_resta.add_argument('a', type=int, help='The first number')
    parser_resta.add_argument('b', type=int, help='The second number')

    args = parser.parse_args()

    if args.command == 'suma':
        resultado = suma(args.a, args.b)
        print(f'The result of adding {args.a} + {args.b} is {resultado}')
    elif args.command == 'resta':
        resultado = resta(args.a, args.b)
        print(f'The result of subtracting {args.b} from {args.a} is {resultado}')
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
