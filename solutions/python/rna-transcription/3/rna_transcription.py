dna_rna = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}


def to_rna(dna_strand: str) -> str:
    return ''.join(dna_rna[item] for item in dna_strand)
