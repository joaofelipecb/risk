import riskApp.p25driver.ProbabilityMultiplicity

class ProbabilityMultiplicity(riskApp.p25driver.ProbabilityMultiplicity.ProbabilityMultiplicity):
    def __init__(self, accounts):
        self.__accounts = accounts
        self.__combinations = []

    @property
    def accounts(self):
        return self.__accounts

    @property
    def combinations(self):
        return self.__combinations

    @combinations.setter
    def combinations(self, combinations):
        self.__combinations = combinations

class CalculateCombinations(riskApp.p25driver.ProbabilityMultiplicity.CalculateCombinations):
    def __init__(self, multiplicity):
        self.__multiplicity = multiplicity
        self.__combinationsLengths = []
        self.__combinationsTuples = []
        self.__combinationsTuplesWithCertainLength = []

    @property
    def multiplicity(self):
        return self.__multiplicity

    @property
    def combinationsLengths(self):
        return self.__combinationsLengths

    @property
    def combinationsTuples(self):
        return self.__combinationsTuples

    @property
    def combinationsTuplesWithCertainLength(self):
        return self.__combinationsTuplesWithCertainLength

    @combinationsLengths.setter
    def combinationsLengths(self, lengths):
        self.__combinationsLengths = lengths

    @combinationsTuplesWithCertainLength.setter
    def combinationsTuplesWithCertainLength(self, combinations):
        self.__combinationsTuplesWithCertainLength = combinations

class Combination(riskApp.p25driver.ProbabilityMultiplicity.Combination):
    def __init__(self, accounts):
        self.__accounts = accounts
        self.__value = 0

    @property
    def accounts(self):
        return self.__accounts

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

