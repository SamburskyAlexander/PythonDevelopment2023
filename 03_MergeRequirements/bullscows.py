import os
import random


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
    print(prompt)

    line = input()
    if valid is None:
        return line

    while line not in valid:
        print("Некорректное слово, должно быть одним из", valid)
        line = input()
        
    return line


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


if __name__ == '__main__':
    pass