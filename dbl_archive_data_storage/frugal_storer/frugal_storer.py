import re

from .frugal_exception import FrugalStorerException
from .frugal_collection import FrugalCollection
from .frugal_key import FrugalKey


class FrugalStorer:
    """
    A class for storing multiple versions of containers in a non-duplicating way.
    """

    collections = None
    hash_keys = None
    id_regex = None

    def __init__(self, regex):
        self.collections = {}
        self.hash_keys = {}
        self.id_regex = regex

    def add_key(self, **spec):
        """
        Adds a key - only allowed when there are no collections.
        """
        if len(self.collections) > 0:
            raise FrugalStorerException("Cannot add keys to non-empty storer")
        if spec["name"] in self.hash_keys:
            raise FrugalStorerException("Cannot redefine existing key {0}".format(spec["name"]))
        if "regex" not in spec:
            raise FrugalStorerException("Regex required for key {0}".format(spec["name"]))
        final_spec = dict(
            name=spec["name"],
            regex=spec["regex"],
            position=len(self.hash_keys),
            required=spec["required"] if "required" in spec else True,
            default = spec["default"] if "default" in spec else None
        )
        self.hash_keys[spec["name"]] = FrugalKey(**final_spec)

    def collection(self, collection_id, mode="fetch"):
        """
        Returns a collection matching the id, or None.

        mode may be "fetch", "create" or "fetch|create".

        * "fetch" will return the collection if it exists, or None if it does not.

        * "create" will return a new container if it does not exist, and raise an error if it does.

        * "fetch|create" will return a matching container if it exists, or new container if it does not.
        """
        if mode not in ["fetch", "create", "fetch|create"]:
            raise FrugalStorerException("Mad mode '{0}' in collection()").format(mode)
        existing_collections = [c for c in self.collections if c.id == collection_id]
        if len(existing_collections) == 0:
            if mode == "fetch":
                return None
            else:
                self._new_collection(collection_id)
        elif mode == "create":
            raise FrugalStorerException("Attempting to create collection that already exists")
        else:
            return existing_collections[0]

    def _new_collection(self, collection_id):
        if not re.search("^{0}$".format(self.id_regex), collection_id):
            raise FrugalStorerException("id for new collection {0} does not match expected format {1}".format(collection_id, self.id_regex))
        self.collections[collection_id] = FrugalCollection(collection_id)
