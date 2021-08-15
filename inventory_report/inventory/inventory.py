from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict

SIMPLE = "simples"
COMPLETE = "completo"


class Inventory:
    def __csv_handler(file_path, type):
        with open(file_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            if type == SIMPLE:
                return SimpleReport.generate(list(reader))
            elif type == COMPLETE:
                return CompleteReport.generate(list(reader))
    """
    :author: Rahel
    __csv_handler(file_path)
        Returns a list of dict using csv entry
    :param file_path: string
    :return: list of dict
    """

    def __json_handler(file_path, type):
        with open(file_path) as json_file:
            reader = json.loads(json_file.read())
            if type == SIMPLE:
                return SimpleReport.generate(list(reader))
            elif type == COMPLETE:
                return CompleteReport.generate(list(reader))
    """
    :author: Rahel
    __json_handler(file_path)
        Returns a list of dict using json entry
    :param file_path: string
    :return: list of dict
    """

    def __xml_handler(file_path, type):
        with open(file_path) as xml_file:
            reader = xmltodict.parse(xml_file.read())
            l_dict = list()
            for item in reader['dataset']['record']:
                l_dict.append(item)
            if type == SIMPLE:
                return SimpleReport.generate(l_dict)
            elif type == COMPLETE:
                return CompleteReport.generate(l_dict)
    """
    :author: Rahel
    __xml_handler(file_path)
        Returns a list of dict using xml entry
    :param file_path: string
    :return: list of dict
    """

    def import_data(path, type):
        if ".csv" in path:
            return Inventory.__csv_handler(path, type)
        elif ".json" in path:
            return Inventory.__json_handler(path, type)
        elif ".xml" in path:
            return Inventory.__xml_handler(path, type)
    """
    :author: Rahel
    import_data(path, type)
        Returns the complete or simple report for path passed
    :param path: string
    :param type: string
    :return: string
    """
