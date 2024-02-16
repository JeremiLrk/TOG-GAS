# ADT Chocolademelk (gemaakt door Tom)
class Chocolademelk:
    maxId = 0

    def __init__(self):
        """
        Initialiseert een Chocolademelk object.

        preconditie: niets
        postconditie: een Chocolademelk object is geïnitialiseerd
        """
        self.id = Chocolademelk.maxId
        self.credits = 5
        self.prijs = 2
        Chocolademelk.maxId += 1

    def addShot(self, chocoladeshot):
        """
        Voeg een chocoladeshot toe aan de chocolademelk.

        preconditie: chocoladeshot is een integer uit [0, 1, 2, 3]
        postconditie: de prijs van de chocolademelk is verhoogd met 1 EUR en de credits zijn verhoogd met 1

        :param chocoladeshot: een integer die de kleur van de chocoladeshot voorstelt:
        0 - WIT
        1 - MELK
        2 - BRUIN
        3 - ZWART
        :return: niets
        """
        pass

    def addTopping(self, topping):
        """
        Voeg een topping toe aan de chocolademelk.

        preconditie: topping is een integer uit [0, 1, 2]
        postconditie: de prijs van de chocolademelk is verhoogd met 1 EUR en de credits zijn verhoogd met 1

        :param topping: een integer die de soort van topping voorstelt:
        0 - Chilipeper
        1 - Honing
        2 - Marshmallow
        :return: niets
        """
        pass

    def getId(self):
        """
        Geeft het ID van de chocolademelk terug.

        preconditie: niets
        postconditie: niets

        :return: het ID van de chocolademelk
        """
        pass

    def getCredits(self):
        """
        Geeft het aantal credits dat de choclademelk kost om te maken terug

        :return: het aantal credits van de chocolademelk
        """
        pass

    def getPrijs(self):
        """
        Geeft de prijs van de choclademelk

        :return: de prijs van de chocolademelk
        """
        pass