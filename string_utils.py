def split_before_each_uppercases(formula):
    start = 0
    split_formula = []
    if len(formula) == 0:
      return []
    else:  
      for i in range(1, len(formula)):
          if formula[i].isupper():
              split_formula.append(formula[start:i])
              start = i

    split_formula.append(formula[start:])
    return split_formula


def split_at_first_digit(formula):
    digit_location = 1
    for ch in formula[1:]:
        if ch.isdigit():
            break
        digit_location += 1
    if digit_location == len(formula):
        return formula, 1
    else:
        prefix = formula[:digit_location]
        numeric_part = int(formula[digit_location:])
        return prefix, numeric_part


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts."""

    
    atom_counts = {}

    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)

        
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count

    
    return atom_counts

