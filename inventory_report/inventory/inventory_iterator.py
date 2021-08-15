from collections.abc import Iterator


class InventoryIterator(Iterator):
    _position: int = None

    def __init__(self, company_collection) -> None:
        self.collection = company_collection
        self.position = 0
    """
    :author: Rahel
    __init__(self, company_collection)
        Instantiate a collection and set the initial position.
    :param company_collection: list
    """

    def __next__(self):
        try:
            value = self.collection[self.position]
            self.position += 1
        except IndexError:
            raise StopIteration()

        return value
    """
    :author: Rahel
    __next__(self):
        Returns a next value from the collections
    """
