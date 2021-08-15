from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if not(".csv" in path):
            raise ValueError("Arquivo inválido")
        else:
            with open(path, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                return list(reader)
    """
    :author: Rahel
    import_data(path)
        Returns a list of dict using csv entry
    :param file_path: string
    :return: list of dict
    """
