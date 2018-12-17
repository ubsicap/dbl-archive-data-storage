class FrugalSnapshot():

    document_properties = None

    def __init__(self, )document_properties:
        self.document_properties = document_properties

    # Moved from storer, needs reworking

    @staticmethod
    def _normalize_keys(collection_keys):
        """
        Returns a dictionary with all values as a list.
        """
        ret = {}
        for collection_key, collection_value in collection_keys.items():
            ret[collection_key] = collection_value if isinstance(collection_value, [list, tuple]) else [collection_key]
        return ret

    def _require_all_keys(self, normalized_keys):
        """
        Raises an exception if all keys are not present.
        """
        for hash_key in self.hash_keys.values():
            if hash_key.name not in normalized_keys and hash_key.required:
                raise FrugalStorerException("Key {0} was not explicitly provided".format(hash_key.name))

    @staticmethod
    def _check_keys(normalized_keys):
        """
        Raises an exception if keys do not match key regex.
        """
        for n_key, n_value in normalized_keys.items():
            if not re.search(
                "^{0}$".format(self.hash_keys[n_key].regex),
                n_value
            ):
                raise FrugalStorerException("Key {0} does not match regex {1}".format(n_key, n_value))

    @staticmethod
    def _add_defaults(normalized_keys):
        """
        Returns a key dictionary with defaults added for missing keys.
        """
        ret = {}
        for hash_key in self.hash_keys.values():
            if hash_key.name in normalized_keys:
                ret[hash_key.name] = normalized_keys[hash_key.name]
            else:
                ret[hash_key.name] = hash_key.default

