import sys
import argparse
from cowsay import cowsay, list_cows

OPTIONALS = set("bdgpstwy")

def main(args):
    if args.l:
        print(list_cows())

    else:
        line_list = []
        for input_line in sys.stdin:
            line_list.append(input_line.strip())
        message = "\n".join(line_list)

        preset = None
        for option, value in args._get_kwargs():
            if option in OPTIONALS and value:
                preset = option
                break

        print(cowsay(
            message=message,
            cow=args.f,
            preset=preset,
            eyes=args.e,
            tongue=args.T,
            width=args.W,
            wrap_text=not args.n),
            file=sys.stdout
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cowsay implementation')

    parser.add_argument("-e", type=str, default='oo', help="string for eyes")
    parser.add_argument("-f", type=str, default='default', help="cow picture file")
    parser.add_argument("-l", action="store_true", help='show list of cows')
    parser.add_argument("-n", action="store_true", help='message with arbitrary whitespaces')
    parser.add_argument("-T", type=str, default='  ', help='string for a tongue')
    parser.add_argument("-W", type=int, default=40, help='width of message picture')

    for option in OPTIONALS:
        parser.add_argument(f"-{option}", action="store_true")

    args = parser.parse_args()

    main(args)