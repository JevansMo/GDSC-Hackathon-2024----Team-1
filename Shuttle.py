from datetime import datetime, date, time, timedelta

class shuttle:

    def __init__(self, dst: int, pop: int, type: str, cap: int):
        # set the instance variables to ints under the assumption that it's easier
        # for html buttons to return ints -Jalen
        self.dst = "LSU" if dst == 0 else "UNO"
        self.pop = pop
        # designates what type shuttle (van or bus) -Jalen
        self.type = type
        # how many people can fit the vehicle -Jalen
        self.cap = cap

    # distance should be given in miles
    def eta_to_xula(self, distance: float) -> time:
        # assuming speed limit is 40mph and converting into seconds -Jalen
        result = datetime.now()
        seconds = (distance/30)*(60**2)
        result += timedelta(seconds=seconds)
        return result.time()