from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):

    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = list()
    """
    :author: Rahel
    __init__(self, importer)
        Instantiate a importer with some import Class and create a empty list
    :param importer: Class
    """

    def __iter__(self) -> InventoryIterator:
        return InventoryIterator(self.data)
    """
    :author: Rahel
    __iter__(self)
        Calls the iterator to the next element
    """

    def import_data(self, path, type):
        self.data.extend(self.importer.import_data(path))
    """
    :author: Rahel
    import_data(self, path)
        Import the data and set it in a parameter
    :param path: string
    :param type: string
    """
