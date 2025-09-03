dna_rna = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}

def to_rna(dna_strand):
    return ''.join(dna_rna[item] for item in dna_strand)
