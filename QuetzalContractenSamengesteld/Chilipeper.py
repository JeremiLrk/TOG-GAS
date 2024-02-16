#ADT chilipeper (combinatie Jasper/Jeremi)
class Chilipeper:
    idcounter = 0

    def __init__(self):
        """
        Constructor voor een Chilipeper object.

        :param id: Uniek identificatienummer van de chilipeper.
        """
        self.id = Chilipeper.idcounter
        self.prijs = 0.25
        self.vervaldatum = None

        Chilipeper.idcounter += 1

    def setVervaldatum(self, date):
        """
        Stel de datum dat de chilipeperportie vervalt in

        :param date: de datum dat deze portie vervalt
        """
        pass

    def isVervallen(self):
        """
        Controleert of de chilipeperportie vervallen is.

        :return: True als de chilipeperportie vervallen is, anders False.
        """
        pass

