import simple_report

MSG_STOCK = "Produtos estocados por empresa:\n"


class CompleteReport(simple_report.SimpleReport):
    @staticmethod
    def generate(data):
        super_return = simple_report.SimpleReport.generate(data)
        companys = dict()
        for report in data:
            if report['nome_da_empresa'] in companys:
                companys[report['nome_da_empresa']] += 1
            else:
                companys[report['nome_da_empresa']] = 1

        final_return = super_return + "\n\n"
        final_return += MSG_STOCK

        for item in companys:
            final_return += "- " + item + ": " + str(companys[item]) + "\n"

        return final_return
        """
        :author: Rahel
        generate(data)
        inherits parent class behavior SimpleReport
        Returns the formatted report received by the data parameter as follows:
            Data de fabricação mais antiga: YYYY-MM-DD
            Data de validade mais próxima: YYYY-MM-DD
            Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA

            Produtos estocados por empresa:
            - Physicians Total Care, Inc.: QUANTIDADE
            - Newton Laboratories, Inc.: QUANTIDADE
            - Forces of Nature: QUANTIDADE

        :param data: list of dict
        :return: string
        """
