import itertools.combinations

def calculate(multiplicity):
    multiplicity.calculate_combinations()

def calculate_combinations(multiplicity):
    multiplicity.calculate_combinations_init()
    for length in range(0,multiplicity.get_accounts_length()+1):
        combinations = itertools.combinations(multiplicity.get_accounts(), length)

        
