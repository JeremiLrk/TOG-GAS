#ADT gebruiker (gemaakt door Jeremi)
class Gebruiker:
    idcounter = 0

    def __init__(self):
        """
        Constructor voor een Gebruiker object.

        :param id: Uniek identificatienummer van de gebruiker.
        """
        self.id = Gebruiker.idcounter  # Het unieke ID voor de gebruiker.
        self.voornaam = None  # Voornaam van de gebruiker.
        self.achternaam = None  # Achternaam van de gebruiker.
        self.emailadres = None  # E-mailadres van de gebruiker.

        Gebruiker.idcounter += 1

    def setNaam(self, voornaam, achternaam):
        """
        Stelt de volledige naam van de gebruiker in.

        Preconditie: voornaam en achternaam moeten strings zijn.
        Postconditie: De voornaam en achternaam van de gebruiker zijn bijgewerkt.

        :param voornaam: De voornaam van de gebruiker.
        :param achternaam: De achternaam van de gebruiker.
        :return: geeft niets terug.
        """
        pass

    def setMailadres(self, emailadres):
        """
        Stelt het e-mailadres van de gebruiker in.

        Preconditie: emailadres moet een geldig e-mailadres zijn.
        Postconditie: Het e-mailadres van de gebruiker is bijgewerkt.

        :param emailadres: Het e-mailadres van de gebruiker.
        :return: geeft niets terug.
        """
        pass

    def getContactgegevens(self):
        """
        Geeft de contactgegevens van de gebruiker terug.

        Preconditie: Geen.
        Postconditie: Geeft de contactgegevens van de gebruiker terug.

        :return: Een tuple met de voornaam, achternaam en het e-mailadres van de gebruiker.
        """
        pass

    def plaatsBestelling(self, bestelling):
        """
        Plaatst een bestelling voor de gebruiker.

        Preconditie: bestelling moet een Bestelling object zijn.
        Postconditie: De bestelling is geplaatst.

        :param bestelling: De bestelling die geplaatst moet worden.
        :return: geeft niets terug.
        """
        pass