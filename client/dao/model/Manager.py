from client.dao.model.CatastropheData import CatastropheData


class Manager:
    def createCatastrohpeData(self,dataRow):
        return CatastropheData(dataRow['fields']['lib_risque_jo'], dataRow['fields']['dat_pub_arrete'], dataRow['fields']['dat_pub_jo'], dataRow['fields']['nom_dept'], dataRow['fields']['nom_region'], dataRow['fields']['lib_commune'], dataRow['fields']['libepci'], dataRow['fields']['dat_deb'], dataRow['fields']['dat_fin'])
