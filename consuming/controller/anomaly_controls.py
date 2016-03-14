
def getAvailableSections(Anomaly, Player):
    """Checks for possible Actions with Anomaly"""
    sectionList = [Quit, Merchant]

    availableSections = list()

    for possibleSection in sectionList:

        try:
            section = possibleSection(Anomaly, Player)

            availableSections.append(section)

        except AttributeError:
            pass

    return availableSections


class AnomalySection:
    """ Each Section of the Anomaly Contains the Interaction Information.
        Currently Implemented:

        Merchant - Buys Goods"""

    def __init__(self, Anomaly, Player):
        # Needs A Init Method which assigns all needed Stats

        # Interaction Type says what you can actualy DO with a Section
        self.interactionType = 'Nothing'
        # Corresponding Player Stats
        self.correspondingStats = {}

    def __call__(self, Anomaly, Player, args):
        # Needs A Call Method which executes the Interaction
        return

    def __iter__(self):
        # For iteration
        return self

    def __len__(self):
        # Number of Possible Interactions
        return 0

    def __getitem__(self, i):
        # i must be an integer
        return None

    def index(self, item):
        # Corresponds to i
        return 0

    def next(self):
        # Iterate Over possible Actions
        raise StopIteration

    def infoString(self):
        # Generate a Information String
        return 'None'


class Quit(AnomalySection):
    def __call__(self, Anomaly, Player):
        quit()

    def infoString(self):
        return 'Quit'


class Merchant(AnomalySection):

    def __init__(self, Anomaly, Player):
        self.goodsForSale = Anomaly.goodsProduced

        self.prices = Anomaly.prices

        self.interactionType = 'Buy'

        self.cursor = -1

        self.correspondingStats = {
            'Cargo Capacity':   Player.currentShip.cargoCapacity,
            'In Cargo Bay':     Player.currentShip.inCargo
        }

    def __call__(self, Anomaly, Player, GoodToBuy, Amount=1):

        if not GoodToBuy:
            return

        if Amount == 0:
            return

        price = self.prices[GoodToBuy]

        Player.spendCredits(price*Amount)

        Player.currentShip.loadCargo(GoodToBuy, Amount)

        return GoodToBuy

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.goodsForSale)

    def __getitem__(self, i):
        return self.goodsForSale[i]

    def index(self, good):
        return self.goodsForSale.index(good)

    def next(self):
        self.cursor += 1

        if self.cursor >= len(self.goodsForSale):
            # Reset Cursor
            self.cursor = -1
            raise StopIteration

        good = self.goodsForSale[self.cursor]

        price = self.prices[good]

        return good, price

    # I think this belongs to viz. Need a better Solution here
    def infoString(self):
        infoStr = ''

        infoStr += 'Merchant - Sells '

        for good in self.goodsForSale:
            infoStr += '%s@%s ' % (good, self.prices[good])

        return infoStr
