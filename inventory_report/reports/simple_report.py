from datetime import date

MSG_OLDER_DATE = "Data de fabricação mais antiga: "
MSG_NEAREST_DATE = "Data de validade mais próxima: "
MSG_COMPANY = "Empresa com maior quantidade de produtos estocados: "


class SimpleReport:
    @staticmethod
    def __date(entry):
        splited = entry.split('-')
        return date(int(splited[0]), int(splited[1]), int(splited[2]))
    """
    :author: Rahel
    __date(entry)
        is a util function to reduce code replication
        Returns a instance of datetime.date
    :param entry: string
    :return: datetime.date
    """
    @staticmethod
    def __nearest(a, b):
        return ((a - date.today()) > (b - date.today()))
    """
    :author: Rahel
    __nearest(entry)
        is a util function to verify if date a is nearest than date b to today
        Returns True if a is nearest than b, and False otherwise
    :param a: datetime.date
    :param b: datetime.date
    :return: Bool
    """
    @staticmethod
    def generate(data):
        today = date.today()
        older_date = date.max
        nearest_exp = date.min
        companys = dict()
        for report in data:
            fabrication = SimpleReport.__date(report['data_de_fabricacao'])
            item_date = SimpleReport.__date(report['data_de_validade'])

            if fabrication < older_date:
                older_date = fabrication

            if (item_date < today) and \
                    SimpleReport.__nearest(item_date, nearest_exp):
                nearest_exp = item_date

            if report['nome_da_empresa'] in companys:
                companys[report['nome_da_empresa']] += 1
            else:
                companys[report['nome_da_empresa']] = 1

        older_return = MSG_OLDER_DATE + str(older_date) + "\n"
        nearest_return = MSG_NEAREST_DATE + str(nearest_exp) + "\n"
        company_return = MSG_COMPANY + max(companys, key=companys.get)
        return older_return + nearest_return + company_return
    """
    :author: Rahel
    generate(data)
        Returns the formatted report received by the data parameter as follows:
            Data de fabricação mais antiga: YYYY-MM-DD
            Data de validade mais próxima: YYYY-MM-DD
            Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA
    :param data: list of dict
    :return: string
    """
