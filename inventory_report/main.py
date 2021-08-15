from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import sys

SIMPLE = "simples"
COMPLETE = "completo"
IMPORTER_EXT = {
    '.csv': CsvImporter,
    '.json': JsonImporter,
    '.xml': XmlImporter
}


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    path = sys.argv[1]
    type_report = sys.argv[2]

    extension = len(path) - path.index('.')
    report = InventoryRefactor(IMPORTER_EXT[path[-extension:]])

    report.import_data(path, type_report)

    if type_report == SIMPLE:
        print(SimpleReport.generate(report.data), end='')
    elif type_report == COMPLETE:
        print(CompleteReport.generate(report.data), end='')
