import os
import random
import argparse
import urllib.request


def bullscows(guess: str, secret: str) -> (int, int):
    bulls_num = 0
    cows_num = 0

    secret_char_set = set(secret)

    for i in range(len(guess)):
        if i < len(secret) and guess[i] == secret[i]:
            bulls_num += 1
        elif guess[i] in secret_char_set:
            cows_num += 1

    return (bulls_num, cows_num)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret_word = random.choice(words)
    tries = 0
    bulls = cows = 0
    guess_word = ''

    while not (bulls == len(secret_word) == len(guess_word)):
        guess_word = ask("Введите слово: ")
        bulls, cows = bullscows(guess_word, secret_word)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        tries += 1

    return tries


def ask(prompt: str, valid: list[str] = None) -> str:
    line = input(prompt)
    if valid is None:
        return line

    while line not in valid:
        line = input(prompt)

    return line


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='bullscows game')

    parser.add_argument("valid_words_src", type=str, help="file or URL with valid words")
    parser.add_argument("length", type=int, default=5, help="length of valid words")

    args = parser.parse_args()

    valid_words = []
    if os.path.exists(args.valid_words_src):
        with open(args.valid_words_src) as f:
            for line in f:
                line = line.strip()
                if len(line) == args.length:
                    valid_words += [line.strip()]
    else:
        with urllib.request.urlopen(args.valid_words_src) as f:
            for line in f:
                line = line.decode().strip()
                if len(line) == args.length:
                    valid_words += [line.strip()]

    tries = gameplay(ask, inform, valid_words)
    print(f"Игра завершена. Число попыток: " + str(tries))