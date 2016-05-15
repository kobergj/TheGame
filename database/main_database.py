import anomaly_db as a_db
import ship_db as sh_db
import starting_stats as st_cf
import content_db as c_db
import view_db as v_db

class DynamicDatabase:

    StartConfiguration = st_cf.StartConfiguration

    Goods = c_db.Goods

    Planets = a_db.Planets

    Spacegates = a_db.Spacegates

    Starbases = a_db.Starbases

    Universe = st_cf.Universe

    Ships = sh_db.Ships

    Enemies = st_cf.Enemies

    Rooms = c_db.Rooms

    TerminalView = v_db.TerminalView
