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


def encrypt_by_number(char: str, shift: int, encrypt: bool = True) -> str:

    max_lower = ord(string.ascii_lowercase[-1])
    min_lower = ord(string.ascii_lowercase[0])
    max_upper = ord(string.ascii_uppercase[-1])
    min_upper = ord(string.ascii_uppercase[0])

    if encrypt is True:
        called_function = encoder_helper
        current = ord(char) + shift
    else:
        called_function = decoder_helper
        current = ord(char) - shift

    if char in string.ascii_lowercase:

        output = called_function(current, min_lower, max_lower)

    elif char in string.ascii_uppercase:

        output = called_function(current, min_upper, max_upper)

    else:
        output = char

    return output


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    output = []

    while len(plaintext) > len(keyword):
        keyword += keyword

    if len(plaintext) != len(keyword):
        keyword = keyword[:len(plaintext)]

    for char, shift in zip(plaintext, keyword):
        output.append(encrypt_by_number(
            char,
            string.ascii_lowercase.index(shift.lower())
        ))

    return ''.join(output)


print(encrypt_vigenere('ATTACKATDAWN', 'LEMON'))


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    output = []

    while len(ciphertext) > len(keyword):
        keyword += keyword

    if len(ciphertext) != len(keyword):
        keyword = keyword[:len(ciphertext)]

    for char, shift in zip(ciphertext, keyword):
        output.append(encrypt_by_number(
            char,
            string.ascii_lowercase.index(shift.lower()),
            encrypt=False
        ))

    return ''.join(output)


print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
