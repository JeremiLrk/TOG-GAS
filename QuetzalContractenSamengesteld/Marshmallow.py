#ADT honing (combinatie Jasper/Jeremi)

class Marshmallow:
    idcounter = 0
    
    def __init__(self):
        """
        Constructor voor een Marshmallow object.
        Het initialiseert de marshmallow met een uniek ID en standaardwaarden voor prijs en vervaldatum.
        """
        self.id = Marshmallow.idcounter  # Het unieke ID voor de marshmallow.
        self.prijs = 0.75  # Standaardprijs van de marshmallow.
        self.vervaldatum = None  # Vervaldatum van de marshmallow.

        Marshmallow.idcounter += 1

    def setVervaldatum(self, date):
        """
        Stel de datum dat de marshmallow vervalt in

        :param date: de datum dat deze marshmallow vervalt
        """
        pass

    def isVervallen(self):
        """
        Controleert of de marshmallow vervallen is.

        :return: True als de marshmallow vervallen is, anders False.
        """
        pass

