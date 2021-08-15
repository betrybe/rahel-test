from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import inventory_report.data
import sys

SIMPLE = "simples"
COMPLETE = "completo"


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
    else:
        print(sys.argv)
        path = sys.argv[1]
        type_report = sys.argv[2]

        if ".csv" in path:
            report = InventoryRefactor(CsvImporter)
        elif ".json" in path:
            report = InventoryRefactor(JsonImporter)
        elif ".xml" in path:
            report = InventoryRefactor(XmlImporter)

        report.import_data(path, type_report)

        if type_report == SIMPLE:
            print(SimpleReport.generate(report.data))
        elif type_report == COMPLETE:
            print(CompleteReport.generate(report.data))
