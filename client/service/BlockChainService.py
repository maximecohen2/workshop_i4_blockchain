from client.dao.BlockChainDAO import BlockChainDAO


class BlockChainService:

    def __init__(self):
        self.blockChainDAO = BlockChainDAO()

    def getCataData(self, commune):
        cataList = self.blockChainDAO.getDataCatastrophe(commune)
        return cataList

