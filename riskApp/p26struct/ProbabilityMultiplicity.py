import riskApp.p25driver.ProbabilityMultiplicity

class ProbabilityMultiplicity(riskApp.p25driver.ProbabilityMultiplicity.ProbabilityMultiplicity):
    def __init__(self, accounts):
        self.__accounts = accounts
        self.__combination = []

