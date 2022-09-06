class Encuesta():
    ANYO = 0
    NOM_PROV = ""
    NOM_MUN = ""
    DESC_CAUSA = ""
    DESC_GENERO = ""
    RANGO_EDAD = ""
    NUM_FALLECIDOS = 0

    def __init__(self, linea):
        self.ANYO = int(linea[0])
        self.NOM_PROV = linea[2]
        self.NOM_MUN = linea[4]
        self.DESC_CAUSA = linea[6]
        self.DESC_GENERO = linea[8]
        self.RANGO_EDAD = linea[9]
        self.NUM_FALLECIDOS = int(linea[-1][:-1])  # '1\n'
    
    def set_from_csv(self, linea):
        self.ANYO = int(linea[0])
        self.NOM_PROV = linea[2]
        self.NOM_MUN = linea[4]
        self.DESC_CAUSA = linea[6]
        self.DESC_GENERO = linea[8]
        self.RANGO_EDAD = linea[9]
        self.NUM_FALLECIDOS = int(linea[-1][:-1])

    def __str__(self):
        return ";".join([str(self.ANYO), self.NOM_PROV,
                         self.NOM_MUN, self.DESC_CAUSA,
                         self.DESC_GENERO, self.RANGO_EDAD,
                         str(self.NUM_FALLECIDOS)])
