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
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    atoms = {}   # Step 1

    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)

        # Step 2
        atoms[atom_name] = atoms.get(atom_name, 0) + atom_count

    # Step 3
    return atoms

