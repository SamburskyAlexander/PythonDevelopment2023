import sys
import argparse
from cowsay import cowsay


# TODO: add -l option

def main(args):
    line_list = []
    for input_line in sys.stdin:
        line_list.append(input_line.strip())
    message = "\n".join(line_list)

    # TODO: add set value of preset

    print(cowsay(
        message=message,
        cow=args.f,
        preset=None,  # use default value for now
        eyes=args.e,
        tongue=args.T,
        width=args.W,
        wrap_text=not args.n)
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cowsay implementation')

    parser.add_argument("-e", type=str, default="oo", help="eyes")
    parser.add_argument("-f", type=str, default="default", help="cow file")
    parser.add_argument("-n", action="store_true", help="arbitrary whitespaces")
    parser.add_argument("-T", type=str, default='  ', help="tongue")
    parser.add_argument("-W", type=int, default=40, help="message width")

    args = parser.parse_args()

    main(args)