class shuttle:

    def __init__(self, dst: int, pop: int):
        # set the instance variables to ints under the assumption that it's easier
        # for html buttons to return ints -Jalen
        self.dst = "LSU" if dst == 0 else self.dst = "UNO"
        self.pop = pop

