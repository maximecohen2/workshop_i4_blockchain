class CatastropheData:

    def __init__(self, typeCatastrophe, datePubArrete, datePubJ, nomDepartement, nomRegion, libelleCommune, libellePci, dateDebutCata, dateFinCata):
        self.typeCatastrophe = typeCatastrophe
        self.datePubArrete = datePubArrete
        self.datePubJ = datePubJ
        self.nomDepartement = nomDepartement
        self.nomRegion = nomRegion
        self.libelleCommune = libelleCommune
        self.libellePci = libellePci
        self.dateDebutCata = dateDebutCata
        self.dateFinCata = dateFinCata

    def _getTypeCatastrophe_(self):
        return self.typeCatastrophe