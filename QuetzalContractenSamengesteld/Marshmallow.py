#ADT honing (combinatie Jasper/Jeremi)

class Marshmallow:
    def __init__(self, id):
        """
        Constructor voor een Marshmallow object.
        Het initialiseert de marshmallow met een uniek ID en standaardwaarden voor prijs en vervaldatum.

        :param id: Uniek identificatienummer van de marshmallow.
        """
        self.id = id  # Het unieke ID voor de marshmallow.
        self.prijs = 0.75  # Standaardprijs van de marshmallow.
        self.vervaldatum = None  # Vervaldatum van de marshmallow.

    def setVervaldatum(self, date):
        """
        Stel de datum dat de marshmallow vervalt in

        :param date: de datum dat deze marshmallow vervalt
        """
        pass

    def isSpoiled(self):
        """
        Controleert of de marshmallow vervallen is.

        :return: True als de marshmallow vervallen is, anders False.
        """
        pass

