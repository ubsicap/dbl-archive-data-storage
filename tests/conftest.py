import pytest


@pytest.fixture
def config():
    rv = {}
    try:
        with open('./config.txt') as fd:
            rv = {}
            for line in fd.readlines():
                components = line.split('=')
                if len(components) > 1:
                    rv[components[0]] = list(*components[1:])
    except Exception as _:
        print('ERROR: no config file read in conftest.config()')
    return rv


@pytest.fixture
def fd_data_storage_path(config):
    return config.get('fs.directory', '/tmp/data_storage_testing')


@pytest.fixture
def fs_data_storage(fd_data_storage_path):
    """ Return a data storage object based on a fs store, reset the store 
    after each use."""
    import os
    import shutil
    from dbl_archive_data_storage import DBLDataStorage

    if not os.path.exists(fd_data_storage_path):
        os.mkdir(fd_data_storage_path)
    yield DBLDataStorage.fs_data_storage(fd_data_storage_path)
    shutil.rmtree(fd_data_storage_path)


@pytest.fixture
def test_entry_uid():
    return 'abcd1234efgh'


def hash_string(string):
    """ return the md5 hash of a string"""
    import hashlib
    return hashlib.md5(string).hexdigest()


def generate_entry_content(name):
    import random
    import string

    content = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(64))
    return (name, hash_string(content), content)


@pytest.fixture
def test_entry_rev1_listing():
    """ return tuples of name, checksum, content for a selection of names.
    content and checksum will change on every run of the code."""
    return [generate_entry_content(name) for name in [
        'releases/foo.xml', 'releases/bar.xml', 'sources/source.zip',
        'releases/metadata.xml', 'foo.usx', 'format.pdf']]


@pytest.fixture
def test_entry_rev2_listing(test_entry_rev1_listing):
    """ as with the rev1 listing fixture, return a list of name, content, 
    checksum. Create the list as a modification of the previous, with some
    deletions, some modifications, and some additions."""
    return test_entry_rev1_listing[1:-2] + [
        generate_entry_content(name) for name in [
            'foo.usx', 'format.pdf', 'new.text', 'image.jpeg']]
