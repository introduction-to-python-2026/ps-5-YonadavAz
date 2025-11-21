


def split_before_uppercases(formula):
    start = 1
    text = []
    for i,x in enumerate(formula):
        if x is isupper():
            text.append[formula[start:i]]
            start = i
        text.append[formula[start:i]]
    return text

def split_at_digit(formula):
    for i,x in enumerate(formula):
        if x is isdigit():
            return formula[:i], formula[i:] 
    return formula, 1

            

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atoms = {}

    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        
        # Step 2: Update the dictionary with the atom name and count
        atoms[atom_name] = atom_count
 
    # Step 3: Return the completed dictionary
    return atoms


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
