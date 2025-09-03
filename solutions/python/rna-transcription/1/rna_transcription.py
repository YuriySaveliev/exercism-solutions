dna_rna = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}

def to_rna(dna_strand):
    rna = ''
    for item in dna_strand:
        rna += dna_rna[item]
    return rna
