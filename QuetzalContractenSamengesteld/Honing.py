#ADT honing (combinatie Jasper/Jeremi)

class Honing:
    idcounter = 0

    def __init__(self):
        """
        Constructor voor een Honing object.
        Het initialiseert de honing met een uniek ID en standaardwaarden voor prijs en vervaldatum.
        """
        self.id = Honing.idcounter  # Het unieke ID voor de honing.
        self.prijs = 0.50  # Standaardprijs van de honing.
        self.vervaldatum = None  # Vervaldatum van de honing.

        Honing.idcounter += 1

    def setVervaldatum(self, date):
        """
        Stel de datum dat deze honingportie vervalt in

        :param date: de datum dat deze portie vervalt
        """
        pass

    def isVervallen(self):
        """
        Controleert of de honingportie vervallen is.

        :return: True als de honingportie vervallen is, anders False.
        """
        pass

