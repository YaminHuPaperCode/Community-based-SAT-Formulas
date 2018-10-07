import random

import Partition
from entity import Clause


class GenerateInstance:
    def __init__(self, n=500, r=4.5, p=0.8, alpha=0.8, c=10, p1=0.6, p2=0.3, s=None):
        # #variables
        self.n = n
        # the ratio of #clauses to #variables
        self.r = r

        # the probability of selecting variables belonging to one community
        self.p = p
        # the ratio of non-overlapping variables
        self.alpha = alpha
        # the number of communities
        self.c = c

        # for p-hidden
        self.p1 = p1
        self.p2 = p2

        # hidden solution
        if s is None:
            self.s = [random.sample(range(2), 1)[0] for _ in range(self.n)]

        # partition nodes into communities
        self.partition = Partition.Partition(self.n, self.c, self.alpha)

        # generate
        self.clauses = self.generateClauses()

    # 1 -> -1; 0 -> 0
    def instanceToFile(self, filename):
        with open(filename, 'w') as f:
            f.write('c a comment\n')
            f.write('p cnf ' + str(self.n) + ' ' + str(len(self.clauses)) + '\n')
            for clauseIndex in range(len(self.clauses)):
                for index in range(len(self.clauses[clauseIndex].polarities)):
                    if self.clauses[clauseIndex].polarities[index] == 1:
                        f.write('-')
                    f.write(str(self.clauses[clauseIndex].variableIndexes[index] + 1))
                    f.write(' ')
                f.write('0\n')

    def generateClauses(self):
        clauses = []
        numClauses = round(self.r * self.n)
        for _ in range(numClauses):
            # get index of 3 variables
            tempRandomNum = random.random()
            if tempRandomNum <= self.p:
                variableIndexes = self.partition.selectVariablesFromOneCommunity()
            else:
                variableIndexes = self.partition.selectVariablesFromThreeCommunity()

            # truth values of the selected variables
            truthValues = [self.s[variableIndexes[0]], self.s[variableIndexes[1]], self.s[variableIndexes[2]]]

            tempRandomNum = random.random()
            if tempRandomNum < self.p1:
                # variables on negative positions is variables to be satisfied
                negativePositions = random.sample(range(3), 1)
            elif tempRandomNum < self.p1 + self.p2:
                negativePositions = random.sample(range(3), 2)
            else:
                negativePositions = random.sample(range(3), 3)

            polarities = GenerateInstance.negatePolaritis(truthValues, negativePositions)

            clause = Clause.Clause()
            clause.variableIndexes = variableIndexes
            clause.polarities = polarities

            clauses.append(clause)

        return clauses

    @ staticmethod
    def negatePolaritis(truthValues, negativePositions):
        polarities = [item for item in truthValues]
        for negativePosition in negativePositions:
            polarities[negativePosition] = 0 if polarities[negativePosition] == 1 else 1
        return polarities
