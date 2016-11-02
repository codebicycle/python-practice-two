
import pytest
from config_dict import ConfigDict


@pytest.fixture()
def file_dict(tmpdir_factory):
    f = tmpdir_factory.mktemp('test').join('config.txt')
    filepath = str(f)
    content = '''one=unu\ntwo=doi\nthree=trei\nfour=patru\n'''
    f.write(content)
    file_dict = ConfigDict(filepath)
    return file_dict


def test_read_keys_from_dict(file_dict):
    assert 'unu'    == file_dict['one']
    assert 'doi'    == file_dict['two']
    assert 'trei'   == file_dict['three']
    assert 'patru'  == file_dict['four']


def test_missing_key_raises_exception(file_dict):
    with pytest.raises(KeyError):
        file_dict['not_in_dict']


def test_add_keys_to_dict(file_dict):
    dict_size = len(file_dict)
    file_dict['nine'] = 'noua'
    file_dict['ten']  = 'zece'

    filepath = file_dict._filepath
    lines    = open(filepath).readlines()
    assert 'ten=zece\n' in lines
    assert 'ten=zece\n' in lines
    assert dict_size + 2 == len(lines)


def test_delete_key_from_dict(file_dict):
    dict_size = len(file_dict)
    del file_dict['two']

    filepath = file_dict._filepath
    lines = open(filepath).readlines()
    assert 'two=doi\n' not in lines
    assert dict_size -1 == len(lines)
