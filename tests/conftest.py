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
def fs_data_storage(config):
    from dbl_archive_data_storage import DataStorage

    return DataStorage.fs_data_storage(
        config.get('fs.directory', '/tmp/data_storage_testing'))


@pytest.fixture
def test_entry_uid():
    return 'abcd1234efgh'
