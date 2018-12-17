from functools import partial


class DBLDataStorage(object):
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
        from .frugal_storer import FSFrugalStorer

        return partial(cls, FSFrugalStorer(root_directory))

    @classmethod
    def s3_data_storage(cls, bucket_name, s3_access_key, s3_secret_key):
        """ Return a partially defined instance around a s3 storage class. """
        from .frugal_storer import S3FrugalStorer

        return partial(
            cls, S3FrugalStorer(bucket_name, s3_access_key, s3_secret_key))

    def __init__(self, storer, entry):
        self.storer = storer
        self.entry = entry

    @property
    def exists(self):
        collection = self.storer.fetch_collection(self.entry)
        return collection is not None

    def revision_exists(self, revision_identifier):
        snapshot = self.storer.fetch_snapshot(revision=revision_identifier)
        return snapshot is not None

    def create_revision(self, revision_identifier, contents):
        """ Create a new revision and describe the contents as a list of 
        resource names and checksums"""
        contents_to_dict = [
            dict(name=name, checksum=checksum) for name, checksum in contents]
        snapshot = self.storer.create_snapshot(
            contents_to_dict, revision=revision_identifier)
        return snapshot

    def ls(self, **specifiers):
        """ Return a list of resources for the entry/revision filtered by the
        provided specifiers. """

        self.storer.snapshot(self.entry, **specifiers).ls()

    def stream(self, resource, **specifiers):
        """ Return an open stream on a resource for the entry/revision filtered
        by the provided specifiers.

        Raise an IOError if the named resource isn't available. """

        return self.storer.snapshot(self.entry, **specifiers).stream(resource)

    def put(self, resource, stream, **specifiers):
        """ Write the contents of a stream to the named resource of an
        entry/revision. specifiers are applied as metadata. """

        return self.storer.snapshot(self.entry, **specifiers).put(resource, stream)

    def stat(self, resource, **specifiers):
        """ Return status info for a resource with specifiers. Stat information 
        should include metadata attributes where defined, as well as expected 
        (implicit) values of checksum, size, revisions, etc."""

        return self.storer.snapshot(self.entry, **specifiers).stat(resource)
