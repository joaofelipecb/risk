import riskApp.p26struct.ProbabilityMultiplicity

def calculate(multiplicity):
    multiplicity.calculate_combinations()

def calculate_combinations(multiplicity):
    calculate = riskApp.p26struct.ProbabilityMultiplicity.CalculateCombinations(multiplicity)
    calculate.generate_combinations_tuples()
    for combinationTuple in calculate.combinationsTuples:
        multiplicity.create_and_append_combination(combinationTuple)

def generate_combinations_tuples(calculate):
    calculate.generate_combinations_tuples_init()
    for combinationsLength in calculate.combinationsLengths:
        calculate.generate_combinations_tuples_with_certain_length(combinationsLength)

def generate_combinations_tuples_with_certain_length(calculate, combinationLength):
    calculate.generate_combinations_tuples_with_certain_length_init(combinationLength)
    for combinationTuple in calculate.combinationsTuplesWithCertainLength:
        calculate.append_combinationTuple(combinationTuple)

def combination_calculate_attributes(combination):
    combination.calculate_value()

def combination_calculate_value(combination):
    for account in combination.accounts:
        combination.sum_account_value(account)


        
