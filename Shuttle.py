from datetime import datetime, date, time, timedelta

class Shuttle:
    def __init__(self, dst: str, pop: int, type: str, cap: int):
        # set the instance variables to ints under the assumption that it's easier
        # for html buttons to return ints -Jalen
        self.dst = dst
        self.pop = pop
        # designates what type shuttle (van or bus) -Jalen
        self.type = type
        # how many people can fit the vehicle -Jalen
        self.cap = cap

    # distance should be given in miles
    def eta_to_xula(self, distance: float, delay: float) -> str:
        # assuming speed limit is 40mph and converting into seconds -Jalen
        now = datetime.now()
        seconds = (distance/20)*(60**2) + delay
        result = (now + timedelta(seconds=seconds)).strftime("%I:%M %p")
        return result