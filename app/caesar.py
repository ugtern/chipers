import typing as tp
import string


def encoder_helper(current: int, minimum: int, maximum: int) -> str:
    if current > maximum:
        return chr(minimum + (current - maximum) - 1)
    else:
        return chr(current)


def decoder_helper(current: int, minimum: int, maximum: int) -> str:
    if current < minimum:
        return chr(maximum - (minimum - current) + 1)
    else:
        return chr(current)


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """

    """
    Caesar encrypt realization
    """

    output = []

    max_lower = ord(string.ascii_lowercase[-1])
    min_lower = ord(string.ascii_lowercase[0])
    max_upper = ord(string.ascii_uppercase[-1])
    min_upper = ord(string.ascii_uppercase[0])

    for char in plaintext:

        current = ord(char) + shift

        if char in string.ascii_lowercase:

            output.append(encoder_helper(current, min_lower, max_lower))

        elif char in string.ascii_uppercase:

            output.append(encoder_helper(current, min_upper, max_upper))

        else:
            output.append(char)

    return ''.join(output)


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """

    output = []

    max_lower = ord(string.ascii_lowercase[-1])
    min_lower = ord(string.ascii_lowercase[0])
    max_upper = ord(string.ascii_uppercase[-1])
    min_upper = ord(string.ascii_uppercase[0])

    for char in ciphertext:

        current = ord(char) - shift

        if char in string.ascii_lowercase:

            output.append(decoder_helper(current, min_lower, max_lower))

        elif char in string.ascii_uppercase:

            output.append(decoder_helper(current, min_upper, max_upper))

        else:
            output.append(char)

    return ''.join(output)


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    encrypt = ciphertext
    while True:
        if encrypt not in dictionary:
            best_shift += 1
            encrypt = decrypt_caesar(ciphertext, best_shift)
        else:
            return best_shift
