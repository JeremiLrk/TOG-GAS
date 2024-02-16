# ADT Reservatiesysteem (gemaakt door Tom)

"""
Hier functies van maken om de datastructuur in te stellen?

from BST import BST
from CDK import LinkedChain
from MyQueue import MyQueue
from MyStack import MyStack
"""


class Reservatiesysteem:
    def __init__(self):
        """
        Initialiseert een Reservatiesysteem object met CDK's voor de gebruikers/werknemers en een queue,
        BST voor respectievelijk de huidigeBestellingen en de verwerkteBestellingen

        preconditie: niets
        postconditie: een Reservatiesysteem object is geïnitialiseerd
        """
        self.gebruikers = LinkedChain()
        self.werknemers = LinkedChain()
        self.actieveWerknemers = MyStack()
        self.huidigeBestellingen = MyQueue()
        self.verwerkteBestellingen = BST()

    def addUGebruiker(self, user):
        """
        Voegt een gebruiker toe aan het reservatiesysteem.

        preconditie: user moet een Gebruiker object zijn
        postconditie: de gebruiker is toegevoegd aan het reservatiesysteem

        :param user: de toe te voegen gebruiker
        :return: niets
        """
        pass

    def addWerknemer(self, user):
        """
        Voegt een werknemer toe aan het reservatiesysteem.

        preconditie: user moet een Werknemer object zijn
        postconditie: de werknemer is toegevoegd aan het reservatiesysteem

        :param user: de toe te voegen werknemer
        :return: niets
        """
        pass

    def addActieveWerknemer(self, user):
        """
        Voegt een actieve werknemer toe aan het reservatiesysteem op de stack.

        preconditie: user moet een Werknemer object zijn
        postconditie: de werknemer is toegevoegd aan het reservatiesysteem

        :param user: de toe te voegen werknemer
        :return: niets
        """
        pass

    def getVolgendeActieveWerknemer(self):
        """
        Verkrijgt de laatst actieve werknemer van de stack en verwijderd deze van de stack

        preconditie: er moet een werknemer op de stack staan
        postconditie: een werknemer is verwijderd van de stack en dus van de actieveWerknemers

        :return: de werknemer die vanboven op de stack staat
        """
        pass

    def addLopendeBestelling(self, order):
        """
        Voegt een lopende bestelling toe aan het reservatiesysteem.

        preconditie: order moet een bestelling zijn
        postconditie: de bestelling is toegevoegd aan de lopende bestellingen

        :param order: de toe te voegen bestelling
        :return: niets
        """
        pass

    def getVolgendeBestelling(self):
        """
        Geeft de eerste bestelling in de wachtrij terug.

        preconditie: er moet minstens één bestelling in de wachtrij zijn
        postconditie: niets

        :return: de eerste bestelling in de wachtrij
        """
        pass

    def addAfgewerkteBestelling(self, order):
        """
        Voegt een voltooide bestelling toe aan het reservatiesysteem.

        preconditie: order moet een voltooide bestelling zijn
        postconditie: de bestelling is toegevoegd aan de voltooide bestellingen

        :param order: de toe te voegen voltooide bestelling
        :return: niets
        """
        pass

    def getWerknemers(self):
        """
        Geeft de werknemers uit de ketting terug

        preconditie: niets
        postconditie: niets

        :return: een lijst van de huidige werknemers
        """
        pass