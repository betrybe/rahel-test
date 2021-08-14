from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv

SIMPLE = "simples"
COMPLETE = "completo"


class Inventory:
    def import_data(path, type):
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if type == SIMPLE:
                return SimpleReport.generate(list(reader))
            elif type == COMPLETE:
                return CompleteReport.generate(list(reader))
    """
    :author: Rahel
    import_data(path, type)
        Returns the complete or simple report for path passed
    :param path: string
    :param type: string
    :return: string
    """
