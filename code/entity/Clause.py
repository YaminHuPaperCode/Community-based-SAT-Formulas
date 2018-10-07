# the structure of a clause
class Clause:
    def __init__(self):
        # the indexes of variables in a clause
        self.variableIndexes = None
        # the popularities of literals in a clause
        # the literal x is in positive polarity; the literal neg(x) is in negative polarity
        self.polarities = None
