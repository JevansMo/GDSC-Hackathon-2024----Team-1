class shuttle:

    def __init__(self, dst: int, pop: int, type: str, cap: int):
        # set the instance variables to ints under the assumption that it's easier
        # for html buttons to return ints -Jalen
        self.dst = "LSU" if dst == 0 else self.dst = "UNO"
        self.pop = pop
        # designates what type shuttle (van or bus) -Jalen
        self.type = type
        # how many people can fit the vehicle -Jalen
        self.cap = cap

