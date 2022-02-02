# Yang Liu
# CMPT 120 D400
# February 2, 2022

def protein():
    amino_acid_count_dictionary = {
        'a': 0,
        'd': 0,
        'f': 0,
        'g': 0,
        'm': 0,
        't': 0,
        'error': 0,
    }

    amino_acid_reference_dictionary = {
        'a': 'Alanine',
        'd': 'Aspartic Acid',
        'f': 'Phenylalanine',
        'g': 'Glycine',
        'm': 'Methionine',
        't': 'Threonine',
    }

    amino_acid_sequence = input('Enter an amino acid sequence: ')
    amino_acid_sequence_length = len(amino_acid_sequence)

    for char in amino_acid_sequence:
        char = char.lower()
        if char in amino_acid_reference_dictionary:
            amino_acid_count_dictionary[char] += 1
        else:
            amino_acid_count_dictionary['error'] += 1

    print(amino_acid_count_dictionary)

    # Get first amino acid letter
    if amino_acid_sequence[0] in amino_acid_reference_dictionary:
        first_amino_acid = amino_acid_sequence[0].upper()
    else:
        first_amino_acid = '*'

    # Get last amino acid letter
    if amino_acid_sequence[-1] in amino_acid_reference_dictionary:
        last_amino_acid = amino_acid_sequence[-1].upper()
    else:
        last_amino_acid = '*'

    # Print out the results


sample_input = 'agtmfrdafmgrtdfph4fdmmaartmfmmt$6'
protein()