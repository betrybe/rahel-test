from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if not(".json" in path):
            raise NameError("Wrong extension error, expected a \'.json\' \
                            and received a " + path.split(".")[1])
        else:
            with open(path) as json_file:
                reader = json.loads(json_file.read())
                return list(reader)
    """
    :author: Rahel
    import_data(path)
        Returns a list of dict using json entry
    :param file_path: string
    :return: list of dict
    """
