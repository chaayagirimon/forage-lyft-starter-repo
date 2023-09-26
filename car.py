from servicable import Servicable
from engine.engine import Engine
from battery.battery import Battery
class Car(Servicable):
    engine = Engine()
    battery = Battery()

    def needs_service():
        pass