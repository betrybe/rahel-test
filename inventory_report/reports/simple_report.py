import datetime
class SimpleReport:
    def __create_date(self, entry):
        splited = entry.split('-')
        return datetime.date(int(splited[0]), int(splited[1]), int(splited[2])) 
    """
    __create_date(self, entry)
        is a util function to reduce code replication
        Returns a instance of datetime.date
    
    :param entry: string
    :return: datetime.date
    """

    def generate(self, data):        
        today = datetime.date.today()        
        older_date = datetime.date.max
        nearest_expiration = datetime.date.min
        companys = {}
        #print(older_date)
        #print(nearest_expiration)
        for report in data:
            manufacturing_date = self.__create_date(report['data_de_fabricacao'])
            expiration_date = self.__create_date(report['data_de_validade'])

            if manufacturing_date < older_date:
                older_date = manufacturing_date
                #print(older_date)
            
            if (not(expiration_date > today)) and ((expiration_date - today) > (nearest_expiration - today)):
                nearest_expiration = expiration_date
                #print(nearest_expiration)
            
            if report['nome_da_empresa'] in companys:
                companys[report['nome_da_empresa']] += 1
            else:
                companys[report['nome_da_empresa']] = 1
                
        formated_report = "Data de fabricação mais antiga: "+str(older_date) +"\n" \
                            +"Data de validade mais próxima: " +str(nearest_expiration) + "\n" \
                                +"Empresa com maior quantidade de produtos estocados: " +max(companys, key=companys.get)
        return formated_report
    """
    generate(self, data)
        Returns the formatted report received by the data parameter as follows:
            Data de fabricação mais antiga: YYYY-MM-DD
            Data de validade mais próxima: YYYY-MM-DD
            Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA
    
    :param data: list of dict
    :return: string
    """