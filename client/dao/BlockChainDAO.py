import json
import requests

from client.dao.model import CatastropheData
from client.dao.model.Manager import Manager


class BlockChainDAO:

    def __init__(self):
        self.baseUrl = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=gaspar-arretes-de-catastrophes-naturelles&q=Talence&rows=10&sort=dat_pub_arrete"
        self.manager = Manager()
    def responseapi(self):
        response = requests.get(self.baseUrl)
        data = json.loads(response.content)
        cataList = [CatastropheData]
        for k in data['records']:
            cataList.append(self.manager.createCatastrohpeData(k))
        return cataList




blockChainDAO = BlockChainDAO()
blockChainDAO.responseapi()