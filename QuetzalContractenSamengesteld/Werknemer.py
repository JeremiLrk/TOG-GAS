# ADT Werknemer (gemaakt door Jeremi)

class Werknemer:
    idcounter = 0
    
    def __init__(self, Workload):
        """
        Constructor voor een Werknemer object.

        """
        self.id = Werknemer.idcounter  # Het unieke ID voor de werknemer.
        self.voornaam = None  # Voornaam van de werknemer.
        self.achternaam = None  # Achternaam van de werknemer.
        self.workload = Workload  # Workload van de werknemer uitgedrukt in credits.

        Werknemer.idcounter += 1

    def setNaam(self, voornaam, achternaam):
        """
        Stelt de volledige naam van de werknemer in.

        Preconditie: voornaam en achternaam moeten strings zijn.
        Postconditie: De voornaam en achternaam van de werknemer zijn bijgewerkt.

        :param voornaam: De voornaam van de werknemer.
        :param achternaam: De achternaam van de werknemer.
        :return: geeft niets terug.
        """
        pass

    def setWorkload(self, workload):
        """
        Stelt de workload van de werknemer in.

        Preconditie: workload moet een positief geheel getal zijn.
        Postconditie: De workload van de werknemer is bijgewerkt.

        :param workload: De nieuwe workload van de werknemer.
        :return: geeft niets terug.
        """
        pass

    def geefBestelling(self, bestelling):
        """
        Koppelt een bestelling aan de werknemer.

        Preconditie: bestelling moet een geldig Bestelling object zijn.
        Postconditie: De bestelling is gekoppeld aan de werknemer.

        :param bestelling: De bestelling die aan de werknemer moet worden gekoppeld.
        :return: geeft niets terug.
        """
        pass

    def isBestellingKlaar(self):
        """
        Controleert of de werknemer klaar is met de bestelling.

        Preconditie: Geen.
        Postconditie: Geen.

        :return: True als de werknemer klaar is, anders False.
        """
        pass

    def verlaagWorkload(self):
        """
        Verlaagt de workload van de werknemer met zijn maximum workload.

        Postconditie: De workload van de werknemer is verlaagd.

        :return: geeft niets terug.
        """
        pass
