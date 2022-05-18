"""Assets."""
from supersetapiclient.base import ObjectFactories

class Assets(ObjectFactories):
    endpoint = "/assets/"
    # Assets is the collection for all Superset assets
    # (databases, datasets, charts, dashboards, saved queries)
    base_object = None

    # Overwrite constructor
    def __init__(self, client):
        self.client = client