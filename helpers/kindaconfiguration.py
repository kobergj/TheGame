
class Currencies:
    # Default Currency
    Credits = "Credits"


class Initial:
    # Name of the Player - Just for Fun
    PlayerName = "Dr. H. Odensaque"
    # Name of the Universe
    UniverseName = "Pegasus"
    # Credits you get on Startup
    StartCredits = 12
    # Initial Ship
    StartShipName = "Enterprise"
    # Initial Cargo Capacity of Ship
    CargoCap = 5
    # Initial Travel Costs of Ship
    TravelCosts = 1


class Stats:
    # The Amount of Cargo you can take with you
    CargoCapacity = "Cargo Capacity"
    # The Cost for an FTL Jump
    TravelCosts = "Travel Costs"


class Cargo:
    # List of Cargo Names
    Names = ['Gin', 'Tobacco', 'Oil', 'BloodySweaters', 'Meat', 'Airplanes', 'Potatoes']


class Harbors:
    # List of Harbor Names
    Names = ['Earth', 'Venus', 'Mars', 'SecretPlanet', 'A3X-424', 'Eden', 'Volcan',
             'Endar', 'Uranus', 'BingoPlanet', 'CrappyWorld', 'CC2', 'LaCathedral',
             'TravelersInn', 'GlibberStation', 'MaggysDiner', 'Nine-Ty-Nine']


class Journey:
    # Don't like it
    NumberOfHarborsToSkipOnTravel = 3


class Layout:
    # Default Size of Buttons
    ButtonSize = 300, 30
    # Font For Texts
    Font = 'arial'
    # Size for Fonts
    FontSize = 20
    # The Amount of Pixels for One Line
    Margin = 30
    # Size of Game Window
    WindowSize = 600, 400


class Images:
    # RGB Tuple Representations of Colors
    Black = 0, 0, 0
    White = 255, 255, 255
    Green = 30, 200, 96
    PurpleLike = 123, 12, 178
    Red = 250, 18, 18

    # # Buy Action # #

    # Identifier for Buy Options
    BuyParent = "Buy ", White
    # Buy Option - Line
    BuyChild = "{} (Buy for {})   ", White
    # Buy Option - Line - Highlighted
    BuyHighlightedChild = "{} (Buy for {})   ", Green

    # # Sell Action # #

    # Identifier for Sell Option
    SellParent = " Sell", White
    # Sell Option - Line
    SellChild = "   {}: {} (Sell for {})", White
    # Sell Option - Line - Highlighted
    SellChild = "   {}: {} (Sell for {})", Green

    class Travel:
        # Next Harbor Message
        Expanded = "Next Locations:"
        # Next Harbor Message - UnExpanded
        UnExpanded = "[Next Locations]"
        # Next Harbor Information
        Line = "{} (Travel for {})"

    class Welcome:
        # Info Message for Welcome
        UnExpanded = " -- Welcome To {} -- "

    class Stats:
        # Current Stats of Player
        UnExpanded = "[Credits] {} [Free Cargo Space] {}"


class Limits:
    # Number of Harbors in Travel Cache
    HarborCache = 5
    # Number of Destination to Choose from
    NumberOfDestinations = 2
    # Price Range - Should be Depended on Item
    PriceRange = [5, 14]


class Logger:
    # Path to Log File
    LogFile = "/Users/Kokweazel/TheGame/logbook.log"
    # File Mode Used - should be 'w' or 'a'
    WriteMode = "w"
    # Level of Log Messages
    Level = "ERROR"
    # Format of Log Messages
    Format = "[%(levelname)s] %(filename)s // %(funcName)s: %(message)s "
    # Message that is shown on Logger Init
    OnInitMessage = 'Logbook Initialized'
    # Message that is shown when function is called
    FuntionInvokedLogMessage = "Function '%s' invoked with args %s and kwargs %s"
    # Message that is show when function is finished
    FunctionFinishedLogMessage = "Function '%s' finished with result %s"
