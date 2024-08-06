from string import digits as DIGITS, punctuation as PUNCTUATION, ascii_letters as LETTERS
from itertools import product
from math import inf, isinf

from tqdm import tqdm


def password_generator(min_length: int = 1, length: None | int = None, max_length: int = inf,
                       digits: bool | str = True, punctuation: bool | str = True, letters: bool | str = True,
                       pattern: str = '') -> str:
    """Подбор пароля"""
    assert isinstance(min_length, int)
    assert length is None or (isinstance(length, int) and 1 <= length)
    assert isinstance(max_length, int) or isinf(max_length)
    assert 1 <= min_length <= max_length
    assert isinstance(digits, bool) or isinstance(digits, str) and all(i in DIGITS for i in digits)
    assert isinstance(punctuation, bool) or isinstance(punctuation, str) and all(i in PUNCTUATION for i in punctuation)
    assert isinstance(letters, bool) or isinstance(letters, str) and all(i in LETTERS for i in letters)
    assert isinstance(pattern, str)

    alphabet = ''
    for alph, ALPH in zip((digits, punctuation, letters), (DIGITS, PUNCTUATION, LETTERS)):
        if isinstance(alph, bool):
            if alph is True:
                alphabet += ALPH
        else:
            alphabet += alph
    alphabet = tuple(alphabet)

    if length is None:
        length = min_length
    else:
        max_length = length

    while length <= max_length:
        for comb in product(alphabet, repeat=length):
            yield ''.join(comb)
        length += 1


if __name__ == '__main__':
    print('7??6?'.split('?'))
    password = '1204ab'
    for p in tqdm(password_generator(min_length=2, max_length=6, digits=True, punctuation=False, letters='ab')):
        if password == p:
            print(f'Password: "{p}"')
            break
    else:
        print('Password not found!')
