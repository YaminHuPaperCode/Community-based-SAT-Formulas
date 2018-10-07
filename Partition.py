import random
import Util
from entity import Variable, Community


# partition variables into c communities
# #non-overlapping variables / #all variables = alpha
class Partition:
    def __init__(self, n, c, alpha):
        self.variables = set([Variable.Variable(i) for i in range(n)])

        # items in self.communities are Variables
        self.communities = set([Community.Community(i) for i in range(c)])

        # step 1

        variableNumInACommunity = n // c
        numCommunityWithPlusOne = n % c
        for community in self.communities:
            # community to node
            if numCommunityWithPlusOne > 0:
                randomVariables = random.sample(self.variables, variableNumInACommunity+1)
                community.variableSet = set(randomVariables)
                self.variables -= set(randomVariables)
                numCommunityWithPlusOne -= 1
            else:
                randomVariables = random.sample(self.variables, variableNumInACommunity)
                community.variableSet = set(randomVariables)
                self.variables -= set(randomVariables)

            # node to community
            for variable in community.variableSet:
                variable.communitySet.add(community)

        # step 2
        nodeNumOfType2InACommunity = round((1-alpha) * n/c)
        randomVariablesType2 = []
        for community in self.communities:
            randomVariablesType2 += random.sample(community.variableSet, nodeNumOfType2InACommunity)

        for variableType2 in randomVariablesType2:
            selfCommunity = list(variableType2.communitySet)[0]
            randomCommunity = Util.selectOtherOne(selfCommunity, self.communities)
            # community to node
            randomCommunity.variableSet.add(variableType2)
            # node to community
            variableType2.communitySet.add(randomCommunity)

    # select 3 variables from one community
    def selectVariablesFromOneCommunity(self):
        targetCommunity = random.sample(self.communities, 1)[0]
        # get all variables in a community; because existing duplicates, use list
        allVariables = []
        for variable in targetCommunity.variableSet:
            if len(variable.communitySet) == 1:
                allVariables.append(variable)
                allVariables.append(variable)
            elif len(variable.communitySet) == 2:
                allVariables.append(variable)
            else:
                assert 1 == 0

        # select 3 different varialbles
        targetVariableIndexes = []
        while len(targetVariableIndexes) != 3:
            randomVariable = random.sample(allVariables, 1)[0]
            if randomVariable.index not in targetVariableIndexes:
                targetVariableIndexes.append(randomVariable.index)
        return targetVariableIndexes


    # select 3 variables from 3 communities
    def selectVariablesFromThreeCommunity(self):
        targetCommunities = random.sample(self.communities, 3)

        communityA = targetCommunities[0]
        communityB = targetCommunities[1]
        communityC = targetCommunities[2]


        allVariables = []
        for variable in communityA.variableSet:
            if len(variable.communitySet) == 1:
                allVariables.append(variable)
                allVariables.append(variable)
            elif len(variable.communitySet) == 2:
                allVariables.append(variable)
            else:
                assert 1 == 0

        for variable in communityB.variableSet:
            if len(variable.communitySet) == 1:
                allVariables.append(variable)
                allVariables.append(variable)
            elif len(variable.communitySet) == 2:
                allVariables.append(variable)
            else:
                assert 1 == 0

        for variable in communityC.variableSet:
            if len(variable.communitySet) == 1:
                allVariables.append(variable)
                allVariables.append(variable)
            elif len(variable.communitySet) == 2:
                allVariables.append(variable)
            else:
                assert 1 == 0

        while True:
            targetVariables = random.sample(allVariables, 3)
            targetVariablesIndexes = [targetVariables[0].index, targetVariables[1].index, targetVariables[2].index]
            if len(set(targetVariablesIndexes)) != 3:
                continue
            if (targetVariables[0] in communityA.variableSet and
                        targetVariables[1] in communityA.variableSet and
                        targetVariables[2] in communityA.variableSet) or \
                    (targetVariables[0] in communityB.variableSet and
                             targetVariables[1] in communityB.variableSet and
                             targetVariables[2] in communityB.variableSet) or \
                    (targetVariables[0] in communityC.variableSet and
                             targetVariables[1] in communityC.variableSet and
                             targetVariables[2] in communityC.variableSet):
                continue
            else:
                break
        return targetVariablesIndexes
        
