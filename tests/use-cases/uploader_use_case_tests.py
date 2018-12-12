import pytest
from .. import fs_data_storage, test_entry_uid


@pytest.xfail
def test_list_all_entry_revision_content(fs_data_storage, test_entry_uid):
    data_storage = fs_data_storage(test_entry_uid)
    all_resources = data_storage.ls()
    assert len(all_resources) == 0
