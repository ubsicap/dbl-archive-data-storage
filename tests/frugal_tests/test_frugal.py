#!/usr/bin/env python3

from dbl_archive_data_storage.frugal_storer import FrugalStorer


f_storer = FrugalStorer(r"[0-9a-f]{16}")
f_storer.add_key(
    name="revision",
    regex="[1-9]\d*"
)
f_storer.add_key(
    name="include_footnotes",
    regex="true|false",
    required=False,
    default="true"
)
f_storer.collection("0123456789abcdef", mode="create")
for f in f_storer.collections.values():
    print("{0}".format(f))
