import datetime
from client.dao.BlockChainDAO import BlockChainDAO
from client.dao.model import CatastropheData


class BlockChainService:

    def __init__(self):
        self.blockChainDAO = BlockChainDAO()

    def getCataData(self):
        cataList = self.blockChainDAO.getDataCatastrophe()
        cataListOfficielToday = self.verifDate(cataList)
        listCommune = self.getListCommune(cataListOfficielToday)
        listTypeCata = self.getListTypeCata(cataListOfficielToday)
        return cataList

    def verifDate(self, catalist):
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        cataListOfficiel = [CatastropheData]
        for cata in catalist:
            if(date == cata.datePubArrete):
                cataListOfficiel.append(cata)
        return cataListOfficiel

    def getListCommune(self, catalist):
        listCommune = []
        for cata in catalist:
            if(listCommune.__contains__(cata.libelleCommune)):
                listCommune.append(cata.libelleCommune)
        return listCommune

    def getListTypeCata(self, catalist):
        listTypeCata = []
        for cata in catalist:
            if(listTypeCata.__contains__(cata.typeCatastrophe)):
                listTypeCata.append(cata.libelleCommune)
        return listTypeCata