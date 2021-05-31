def create_and_append_combination(multiplicity, combinationTuple):
    import riskApp.p26struct.ProbabilityMultiplicity
    combination = riskApp.p26struct.ProbabilityMultiplicity.Combination(combinationTuple)
    combination.calculate_attributes()
    multiplicity.combinations.append(combination)

def generate_combinations_tuples_init(calculate):
    accounts = calculate.multiplicity.accounts
    calculate.combinationsLengths = range(0, len(accounts) + 1)

def generate_combinations_tuples_with_certain_length_init(calculate, length):
    import itertools
    accounts = calculate.multiplicity.accounts
    combinations = itertools.combinations(accounts, length)
    calculate.combinationsTuplesWithCertainLength = combinations

def append_combinationTuple(calculate, combinationTuple):
    calculate.combinationsTuples.append(combinationTuple)

def calculate_combinations_aggregate(multiplicity, length):
    import itertools
    combinations = list(itertools.combinations(multiplicity.accounts, length))
    multiplicity.combinations += combinations

def combination_sum_account_value(combination, account):
    combination.value += account.value

