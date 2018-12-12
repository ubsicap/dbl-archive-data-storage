import pytest
from ..conftest import (
    fs_data_storage, test_entry_uid, test_entry_rev1_listing,
    test_entry_rev2_listing)


def test_smoke_test():
    """ This exists only to make sure tests are running"""
    assert True


@pytest.mark.xfail(raises=ModuleNotFoundError)
def test_list_all_entry_content(fs_data_storage, test_entry_uid):
    """ Test that the test_entry_uid entry has no contents. """
    data_storage = fs_data_storage(test_entry_uid)
    all_resources = data_storage.ls()
    assert len(all_resources) == 0


@pytest.mark.xfail(raises=ModuleNotFoundError)
def test_list_all_entry_revision_content(fs_data_storage, test_entry_uid):
    """ Test that the first revision of test_entry_uid has no contents."""
    data_storage = fs_data_storage(test_entry_uid)
    all_resources = data_storage.ls(revision='1')
    assert len(all_resources) == 0


@pytest.mark.xfail(raises=ModuleNotFoundError)
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


@pytest.mark.xfail(raises=ModuleNotFoundError)
def test_insert_revision_2(
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

    # list all contents of the snapshot, ensure that they match up with
    # expectations.
    all_resources = data_storage.ls(revision='1')
    assert len(all_resources) == len(test_entry_rev1_listing)
    for resource_name, checksum, content in test_entry_rev1_listing:
        assert resource_name in all_resources
        stat = data_storage.stat(resource_name)
        assert 'checksum' in stat and stat['checksum'] == checksum
        assert data_storage.stream(resource_name).read() == content
