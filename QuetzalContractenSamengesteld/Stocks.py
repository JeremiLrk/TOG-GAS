# ADT Stocks (combinatie Jens/Tom)

class Stocks:
    def __init__(self):
        """
        Initialiseert een Stocks object met lege lijsten voor verschillende producten.

        preconditie: niets
        postconditie: een Stocks object is geïnitialiseerd
        """
        self.chocoladeshots = []
        self.honingporties = []
        self.marshmallows = []
        self.chilipeperporties = []

    def addToStock(self, product):
        """
        Voegt een product toe aan de voorraad.

        preconditie: product moet een geldig product zijn
        postconditie: het product is toegevoegd aan de voorraad

        :param product: het toe te voegen product
        :return: niets
        """
        pass

    def removeFromStock(self, productType):
        """
        Verwijdert een product uit de voorraad.

        preconditie: productType is een integer uit [0, 1, 2, 3]
        postconditie: een product is verwijderd uit de voorraad

        :parma productType: een integer die het type product voorstelt:
        0 - Chilipeper
        1 - Honing
        2 - Marshmallow
        3 - Chocoladeshot
        :return: niets
        """
        pass

    def getSortedProducts(self):
        """
        Geeft een gesorteerde lijst van producten terug.

        preconditie: niets
        postconditie: niets

        :return: een gesorteerde lijst van producten
        """
        pass

    def getStockAmounts(self, stock):
        pass
        '''
        krijg het aantal items uit een bepaalde stock
        Preconditie: /
        Postconditie: /
        Parameters: stock: een integer voor de stock waarvaan je aantal items wil
        0 = Chocolade
        1 = Honing
        2 = Marshmellows
        3 = Chili

        :return: aantal items is een integer
        '''