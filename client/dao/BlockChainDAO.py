import json
import requests

from urllib.parse import urlencode
from client.dao.model import CatastropheData
from client.dao.model.Manager import Manager


class BlockChainDAO:

    def __init__(self):
        self.baseUrl = "https://public.opendatasoft.com/api/records/1.0/search/"
        self.manager = Manager()

    def getDataCatastrophe(self, commmune):
        urlParams = self.buildParamsUrl(commmune)
        return self.responseapi(urlParams)

    def buildParamsUrl(self, commune):
        params = {}
        params['dataset'] = "gaspar-arretes-de-catastrophes-naturelles"
        params['q'] = commune
        params['rows'] = 15
        params['sort'] = "dat_pub_arrete"
        return params

    def responseapi(self, paramsUrl):
        urlEncode = urlencode(paramsUrl)
        url = self.baseUrl + '?' + urlEncode
        response = requests.get(url)
        data = json.loads(response.content)
        cataList = [CatastropheData]
        for k in data['records']:
            cataList.append(self.manager.createCatastrohpeData(k))
        return cataList




blockChainDAO = BlockChainDAO()
blockChainDAO.getDataCatastrophe("Talence")