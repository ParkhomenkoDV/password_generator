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

    if not pattern:
        while length <= max_length:
            for comb in product(alphabet, repeat=length):
                yield ''.join(comb)
            length += 1
    else:  # TODO: переделать по правилам регулярных выражений
        length = pattern.count('?')
        question_indices = tuple(i for i, char in enumerate(pattern) if char == '?')  # индексы позиций '?'
        for comb in product(alphabet, repeat=length):
            p = list(pattern)
            for idx, el in zip(question_indices, comb):
                p[idx] = el
            yield ''.join(p)


if __name__ == '__main__':

    testing = dict()

    if 1:
        testing['1204'] = {'length': 4,
                           'digits': True, 'punctuation': False, 'letters': False}

    if 1:
        testing['1204ab'] = {'min_length': 2, 'max_length': 6,
                             'digits': True, 'punctuation': False, 'letters': 'ab',
                             'pattern': '1???a?'}

    for password, kwargs in testing.items():
        for p in tqdm(password_generator(**kwargs)):
            if password == p:
                print(f'Password: "{p}"')
                break
        else:
            print('Password not found!')
