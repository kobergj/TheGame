import anomaly_db as a_db
import ship_db as sh_db
import starting_stats as st_cf
import content_db as c_db
import view_db as v_db
import game_config as g_cf


class Database:

    StartConfiguration = st_cf.StartConfiguration

    Goods = c_db.Goods

    Anomalies = a_db.Anomalies

    Rooms = c_db.Rooms

    # Planets = a_db.Planets

    # Spacegates = a_db.Spacegates

    # Starbases = a_db.Starbases

    # Universe = st_cf.Universe

    # Ships = sh_db.Ships

    # Enemies = st_cf.Enemies

    # Rooms = c_db.Rooms

    TerminalView = v_db.TerminalView

