#!/usr/bin/python3

import argparse
import sys
from rich import print

# quip modules
from quip.generate import Generate


def main(args):
    print("[>>] Generating password...")
    generator = Generate(
        args.length, args.include_special, args.no_digits)
    password = generator.password_candidate()
    print("[>>] Password generated: [bold green]\n{}[/bold green]".format(password))


def print_banner():
    print("""[bold cyan] 
╔═╗ ╦ ╦╦╔═╗
║═╬╗║ ║║╠═╝
╚═╝╚╚═╝╩╩  

    [/bold cyan]""")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=print_banner(),
        epilog=">> Quick passwords as you need them"
    )

    parser.add_argument('-s', '--special',
                        action=argparse.BooleanOptionalAction,
                        dest='include_special',
                        help='include special characters')

    parser.add_argument('-l', '--length',
                        dest='length',
                        type=int,
                        help='password length')

    parser.add_argument('-nd', '--no-digits',
                        action=argparse.BooleanOptionalAction,
                        dest='no_digits',
                        help='exclude digits')

    args = parser.parse_args()

    main(args)
