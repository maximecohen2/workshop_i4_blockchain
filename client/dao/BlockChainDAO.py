import json
import requests



class BlockChainDAO:

    def __init__(self):
        self.baseUrl = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=gaspar-arretes-de-catastrophes-naturelles&q=Talence&rows=10&sort=dat_pub_arrete"

    def responseapi(self):
        response = requests.get(self.baseUrl)
        print(response.)

blockChainDAO = BlockChainDAO()
blockChainDAO.responseapi()