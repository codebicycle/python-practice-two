"""
--- Day 14: One-Time Pad ---

In order to communicate securely with Santa while you're on this mission, you've been using a one-time pad that you generate using a pre-agreed algorithm. Unfortunately, you've run out of keys in your one-time pad, and so you need to generate some more.

To generate keys, you first get a stream of random data by taking the MD5 of a pre-arranged salt (your puzzle input) and an increasing integer index (starting with 0, and represented in decimal); the resulting MD5 hash should be represented as a string of lowercase hexadecimal digits.

However, not all of these MD5 hashes are keys, and you need 64 new keys for your one-time pad. A hash is a key only if:

    It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
    One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.

Considering future hashes for five-of-a-kind sequences does not cause those hashes to be skipped; instead, regardless of whether the current hash is a key, always resume testing for keys starting with the very next hash.

For example, if the pre-arranged salt is abc:

    The first index which produces a triple is 18, because the MD5 hash of abc18 contains ...cc38887a5.... However, index 18 does not count as a key for your one-time pad, because none of the next thousand hashes (index 19 through index 1018) contain 88888.
    The next index which produces a triple is 39; the hash of abc39 contains eee. It is also the first key: one of the next thousand hashes (the one at index 816) contains eeeee.
    None of the next six triples are keys, but the one after that, at index 92, is: it contains 999 and index 200 contains 99999.
    Eventually, index 22728 meets all of the criteria to generate the 64th key.

So, using our example salt of abc, index 22728 produces the 64th key.

Given the actual salt in your puzzle input, what index produces your 64th one-time pad key?

Your puzzle input is ngcjuoqr.

"""
import hashlib
import re
import collections

THREE_ROW = re.compile(r'(\w)\1\1')


def generate_hashes(salt):
    if isinstance(salt, str):
        salt = bytes(salt, 'utf8')

    index = 0
    while True:
        message = salt + bytes(str(index), 'utf8')
        digest = hashlib.md5(message).hexdigest()
        yield digest, index
        index += 1


def next_batch(generator, batch_size):
    return [next(generator) for _ in range(batch_size)]


def get_keys(generator):
    buffer = collections.deque()
    keys = []
    while len(keys) < 64:
        if not buffer:
            buffer.append(next(generator))

        digest, index = buffer.popleft()
        match = THREE_ROW.search(digest)
        if match:
            char = match.group(1)
            keyword = char * 5

            new_items = next_batch(generator, 1000 - len(buffer))
            buffer.extend(new_items)

            if any(keyword in next_digest
                   for next_digest, _ in buffer):
                key = digest, index
                keys.append(key)

    return keys


def main():
    # # Example
    salt = 'abc'
    hash_generator = generate_hashes(salt)
    keys = get_keys(hash_generator)
    last_digest, last_index = keys[-1]
    print(last_index)

    # # Problem input
    salt = 'ngcjuoqr'
    hash_generator = generate_hashes(salt)
    keys = get_keys(hash_generator)
    last_digest, last_index = keys[-1]
    print(last_index)


if __name__ == '__main__':
    main()
