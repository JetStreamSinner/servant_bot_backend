class ServiceInfoProvider:

    def __init__(self):
        self.uri = ""
        self.source = {}

    def read(self, uri: str):
        raise RuntimeError("Need to implement")

    def get_as_json(self):
        return self.source
