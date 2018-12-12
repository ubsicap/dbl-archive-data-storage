from functools import partial


class DataStorage(object):
    """
    An interface class for talking to the underlying storage engine.

    The class is initialized to a storage class, entry id (uid), and revision
    string. The class provides high-level methods for listing, querying, getting
    and setting contents.
    """

    @classmethod
    def fs_data_storage(cls, root_directory):
        """ Return a partially defined instance around a file-system storage
        class"""
        from frugal_storer import FSFrugalStorer

        return partial(DataStorage, FSFrugalStorer(root_directory))

    @classmethod
    def s3_data_storage(cls, bucket_name, s3_access_key, s3_secret_key):
        """ Return a partially defined instance around a s3 storage class. """
        from frugal_storer import S3FrugalStorer

        return partial(DataStorage, S3FrugalStorer(bucket_name, s3_access_key, s3_secret_key))

    def __init__(self, frugal_storer, entry):
        self.storer = frugal_storer
        self.entry = entry

    def ls(self, **specifiers):
        """ Return a list of resources for the entry/revision filtered by the
        provided specifiers. """

        pass

    def stream(self, resource, **specifiers):
        """ Return an open stream on a resource for the entry/revision filtered
        by the provided specifiers.

        Raise an IOError if the named resource isn't available. """

        pass

    def put(self, resource, stream, **specifiers):
        """ Write the contents of a stream to the named resource of an
        entry/revision. specifiers are applied as metadata. """

        pass

    def stat(self, resource, **specifiers):
        """ Return status info for a resource with specifiers. Stat information 
        should include metadata attributes where defined, as well as expected 
        (implicit) values of checksum, size, revisions, etc."""

        pass
