#ADT honing (combinatie Jasper/Jeremi)

class Honing:
    def __init__(self, id):
        """
        Constructor voor een Honing object.
        Het initialiseert de honing met een uniek ID en standaardwaarden voor prijs en vervaldatum.

        :param id: Uniek identificatienummer van de honing.
        """
        self.id = id  # Het unieke ID voor de honing.
        self.prijs = 0.50  # Standaardprijs van de honing.
        self.vervaldatum = None  # Vervaldatum van de honing.

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

