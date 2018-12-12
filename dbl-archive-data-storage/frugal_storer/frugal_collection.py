class FrugalCollection:
    
    id = None
    snapshots = None

    def __init__(self, collection_id):
        snapshots = {}
        self.id = collection_id

    def __str__(self):
        return "<Collection {0}>".format(self.id)