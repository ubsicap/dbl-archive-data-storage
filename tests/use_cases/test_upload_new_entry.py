import pytest
from ..conftest import (
    fs_data_storage, test_entry_uid, test_entry_rev1_listing,
    test_entry_rev2_listing)


@pytest.mark.xfail(raises=ImportError)
def test_insert_revision_1(
        fs_data_storage, test_entry_uid, test_entry_rev1_listing):
    """ Take a list of names and content from the rev1 listing and insert them 
    into the data store. """
    from io import StringIO

    # first ensure that the rev does not exist.
    data_storage = fs_data_storage(test_entry_uid)
    all_resources = data_storage.ls(revision='1')
    assert len(all_resources) == 0

    # for each resource in the 'bundle', insert the content
    for resource_name, checksum, content in test_entry_rev1_listing:
        data_storage.put(
            resource_name, StringIO(content), checksum=checksum, revision='1')

    all_resources = data_storage.ls(revision='1')
    assert len(all_resources) == len(test_entry_rev1_listing)
    for resource_name, checksum, content in test_entry_rev1_listing:
        assert resource_name in all_resources
        stat = data_storage.stat(resource_name)
        assert 'checksum' in stat and stat['checksum'] == checksum
        assert data_storage.stream(resource_name).read() == content


@pytest.mark.xfail(raises=ImportError)
def test_insert_revision_2(
        fs_data_storage, test_entry_uid, test_entry_rev2_listing):
    """ Take a list of names and content from the rev2 listing and insert them 
    into the data store. """
    from io import StringIO

    # first ensure that the rev does not exist.
    data_storage = fs_data_storage(test_entry_uid)
    all_resources = data_storage.ls(revision='2')
    assert len(all_resources) == 0

    # for each resource in the 'bundle', insert the content
    for resource_name, checksum, content in test_entry_rev2_listing:
        data_storage.put(
            resource_name, StringIO(content), checksum=checksum, revision='1')

    # list all contents of the snapshot, ensure that they match up with
    # expectations.
    all_resources = data_storage.ls(revision='2')
    assert len(all_resources) == len(test_entry_rev1_listing)
    for resource_name, checksum, content in test_entry_rev2_listing:
        assert resource_name in all_resources
        stat = data_storage.stat(resource_name)
        assert 'checksum' in stat and stat['checksum'] == checksum
        assert data_storage.stream(resource_name).read() == content
