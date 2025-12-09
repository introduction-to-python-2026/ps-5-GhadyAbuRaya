def split_before_uppercases(formula):
    elements = []
    current = ""

    for char in formula:
        if char.isupper():
            if current:
                elements.append(current)
            current = char
        else:
            current += char

    if current:
        elements.append(current)

    return elements


def split_at_digit(formula):
    name = ""
    num = ""

    for c in formula:
        if c.isdigit():
            num += c
        else:
            name += c

    return name, int(num) if num else 1


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts."""

    
    atom_counts = {}

    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)

        
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count

    
    return atom_counts

