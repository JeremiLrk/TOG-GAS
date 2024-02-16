#ADT chocoladeshot (combinatie Jasper/Jeremi)
class Chocoladeshot:
    idcounter = 0

    def __init__(self):
        """
        Constructor voor een Chocoladeshot object.
        Het initialiseert de chocoladeshot met een uniek ID en standaardwaarden voor type, prijs en vervaldatum.

        :param id: Uniek identificatienummer van de chocoladeshot.
        """
        self.id = Chocoladeshot.idcounter  # Het unieke ID voor de chocoladeshot.
        self.type = None  # Type van de chocoladeshot, bijvoorbeeld WIT, MELK, BRUIN, ZWART.
        self.prijs = 1  # Standaardprijs van de chocoladeshot.
        self.vervaldatum = None  # Vervaldatum van de chocoladeshot.

        Chocoladeshot.idcounter += 1

    def setVervaldatum(self, date):
        """
        Stel de datum dat dit chocoladeshot vervalt in

        :param date: de datum dat dit chocoladeshot vervalt
        """
        pass

    def isVervallen(self):
        """
        Controleert of de chocoladeshot vervallen is.

        :return: True als de chocoladeshot vervallen is, anders False.
        """
        pass

