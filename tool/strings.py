import random
import string
import itertools

def randstr(n=4, fixed=True, charset=None):

    if not n:
        return ''

    if not fixed:
        n = random.randint(1, n)

    if not charset:
        charset = string.letters + string.digits

    return ''.join(random.choice(charset) for x in range(n))

def divide(str, min_size, max_size, split_size):
    it = iter(str)
    size = len(str)
    for i in range(split_size - 1, 0, -1):
        s = random.randint(min_size, size - max_size * i)
        yield ''.join(itertools.islice(it, 0, s))
        size -= s
    yield ''.join(it)

def sxor(s1, s2):
    return ''.join(
        chr(ord(a) ^ ord(b))
        for a, b in zip(s1, itertools.cycle(s2))
    )
