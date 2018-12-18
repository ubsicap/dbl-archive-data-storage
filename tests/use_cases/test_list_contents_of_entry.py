""" Tests to excercise the library's ability to list contents of an entry, both
by entry and by revision. 

Further tests exercise the ability to filter by (e.g.) booklist."""

import pytest
from ..conftest import (
    fs_data_storage, test_entry_uid, test_entry_rev1_listing,
    test_entry_rev2_listing)


@pytest.mark.xfail(raises=ImportError)
def test_list_all_entry_content(fs_data_storage, test_entry_uid):
    """ Test that the test_entry_uid entry has no contents. """
    data_storage = fs_data_storage(test_entry_uid)
    all_resources = data_storage.ls()
    assert len(all_resources) == 0


@pytest.mark.xfail(raises=ImportError)
def test_list_all_entry_revision_content(fs_data_storage, test_entry_uid):
    """ Test that the first revision of test_entry_uid has no contents."""
    data_storage = fs_data_storage(test_entry_uid)
    all_resources = data_storage.ls(revision='1')
    assert len(all_resources) == 0
