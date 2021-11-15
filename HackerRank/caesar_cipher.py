import string


def caesarCipher(text, k):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    alphabet_size = len(lowercase)
    idx_map = {i: (i+k) % alphabet_size for i in range(alphabet_size)}

    accumulator = []
    for letter in text:
        if letter.islower():
            original_idx = lowercase.index(letter)
            new_idx = idx_map[original_idx]
            accumulator.append(lowercase[new_idx])
        elif letter.isupper():
            original_idx = uppercase.index(letter)
            new_idx = idx_map[original_idx]
            accumulator.append(uppercase[new_idx])
        else:
            accumulator.append(letter)

    return ''.join(accumulator)


def caesarCipher(text, k):
    alphabet = string.ascii_lowercase

    mapping = {}
    for idx, letter in enumerate(alphabet):
        new_idx = (idx + k) % len(alphabet)
        mapping[letter] = alphabet[new_idx]

    upper_mapping = {key.upper(): val.upper() for (key, val) in mapping.items()}
    mapping.update(upper_mapping)

    accumulator = [mapping.get(letter, letter) for letter in text]
    return ''.join(accumulator)


if __name__ == '__main__':
    text = 'middle-Outz'
    k = 2
    expected = 'okffng-Qwvb'
    assert caesarCipher(text, k) == expected
