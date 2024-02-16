# ADT Chocolademelk (gemaakt door Jeremi)
class Bestelling:
    idcounter = 0

    def __init__(self, timestamp):
        """
        Constructor voor een Bestelling object.

        :param id: Uniek identificatienummer van de bestelling.
        """
        self.id = Bestelling.idcounter  # Het unieke ID voor de bestelling.
        self.gebruikersid = None  # ID van de gebruiker die de bestelling plaatst.
        self.timestamp = timestamp  # Tijdstip van de bestelling.
        self.chocolademelkid = None  # ID van de bestelde chocolademelk.
        self.afgehaald = False  # Status van afhaling van de bestelling.

        Bestelling.idcounter += 1

    def setGebruiker(self, gebruikersid):
        """
        Koppelt een gebruiker aan de bestelling.

        Preconditie: gebruikersid moet een geldig identificatienummer zijn.
        Postconditie: De bestelling is gekoppeld aan een specifieke gebruiker.

        :param gebruikersid: Het ID van de gebruiker die de bestelling plaatst.
        :return: geeft niets terug.
        """
        pass
    def setToAfgehaald(self):
        """
        Markeert de bestelling als afgehaald.

        Preconditie: Geen.
        Postconditie: De bestelling is gemarkeerd als afgehaald.

        :return: geeft niets terug.
        """
        pass

    def setChocolademelk(self, chocolademelkid):
        """
        Koppelt een chocolademelk aan de bestelling.

        Preconditie: chocolademelkid moet een geldig identificatienummer van een chocolademelk zijn.
        Postconditie: De bestelling is gekoppeld aan een specifieke chocolademelk.

        :param chocolademelkid: Het ID van de bestelde chocolademelk.
        :return: geeft niets terug.
        """
        pass

    def setTijd(self, tijd):
        """
        Stelt de tijd van de bestelling in.

        Preconditie: tijd moet een geldige datumtijdrepresentatie zijn.
        Postconditie: De tijd van de bestelling is ingesteld.

        :param tijd: Het tijdstip waarop de bestelling gezet moet worden.
        :return: geeft niets terug.
        """
        pass
