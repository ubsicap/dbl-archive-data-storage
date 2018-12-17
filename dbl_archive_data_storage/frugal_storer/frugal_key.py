class FrugalKey():

    name = None
    regex = None
    position = None
    required = None
    default = None

    def __init__(self, **spec):
        self.name = spec["name"]
        self.regex = spec["regex"]
        self.position = spec["position"]
        self.required = spec["required"]
        self.default = spec["default"]
