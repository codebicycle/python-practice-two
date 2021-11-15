import pytest

from huffman import Huffman


def test_huffman_encode_decode_reverse():
    initial = 'A man, a plan, a canal, Panama'
    huffman = Huffman(initial)

    message = initial
    encoded = huffman.encode(message)
    decoded = huffman.decode(encoded)
    assert message == decoded

    message = 'nana'
    encoded = huffman.encode(message)
    decoded = huffman.decode(encoded)
    assert message == decoded


def test_huffman_init_only_one_symbol():
    huffman = Huffman('a')
    assert '0' == huffman.encode('a')


def test_huffman_init_empty_string():
    with pytest.raises(ValueError):
        Huffman('')
