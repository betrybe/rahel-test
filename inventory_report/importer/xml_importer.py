from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        if not(".xml" in path):
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as xml_file:
                reader = xmltodict.parse(xml_file.read())
                l_dict = list()
                for item in reader['dataset']['record']:
                    l_dict.append(item)
                return l_dict
    """
    :author: Rahel
    import_data(path)
        Returns a list of dict using xml entry
    :param file_path: string
    :return: list of dict
    """
