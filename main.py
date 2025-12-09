from string_utils import (
    split_before_uppercases,
    split_at_digit,
    count_atoms_in_molecule,
    parse_chemical_reaction,
    count_atoms_in_reaction,
)

from equation_utils import build_equations, my_solve





def balance_reaction(reaction):
    # 1. parse reaction
    reactants, products = parse_chemical_reaction(reaction)
    reactant_atoms = count_atoms_in_reaction(reactants)
    product_atoms = count_atoms_in_reaction(products)

    # 2. build equations and solve
    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    solved_coeffs = my_solve(equations, coefficients)

    # 3. add the last product coefficient (which is fixed to 1 in build_equations)
    return solved_coeffs + [1]


