# the structure of a variable
class Variable:
    def __init__(self, index):
        # the index of this variable
        self.index = index
        # the communities that this variable belongs to
        self.communitySet = set()
