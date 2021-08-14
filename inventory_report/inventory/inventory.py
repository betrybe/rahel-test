from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json

SIMPLE = "simples"
COMPLETE = "completo"


class Inventory:
    def __csv_handler(file_path):
        with open(file_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            return list(reader)
    """
    :author: Rahel
    __csv_handler(file_path)
        Returns a list of dict using csv entry
    :param file_path: string
    :return: list of dict
    """

    def __json_handler(file_path):
        with open(file_path) as json_file:
            reader = json.loads(json_file.read())
            return list(reader)
    """
    :author: Rahel
    __json_handler(file_path)
        Returns a list of dict using json entry
    :param file_path: string
    :return: list of dict
    """

    def import_data(path, type):
        if ".csv" in path:
            report = Inventory.__csv_handler(path)
        elif ".json" in path:
            report = Inventory.__json_handler(path)

        if type == SIMPLE:
            return SimpleReport.generate(report)
        elif type == COMPLETE:
            return CompleteReport.generate(report)
    """
    :author: Rahel
    import_data(path, type)
        Returns the complete or simple report for path passed
    :param path: string
    :param type: string
    :return: string
    """

# print(Inventory.import_data("C:/Users/isaac/Desktop/trybe/rahel-test/inventory_report/data/inventory.csv", "completo"))
