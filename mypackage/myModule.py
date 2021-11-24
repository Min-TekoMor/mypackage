def dna_complementary(dna):

    """ Find the complementary strands of DNA given

A links with T and vice versa C links with G and vice versa

Args:
    dna (string): made up of neuclotides of varying lengths

Returns:
        A string of complementary neuclotides

        Example:
        complementary_dna('ATGCTA')== 'TACGAT'
"""

    complementary_dna = ''
    for x in dna:
        if x == 'A':
            complementary_dna+='T'
        if x == 'C':
            complementary_dna+='G'
        if x == 'G':
            complementary_dna+='C'
        if x == 'T':
            complementary_dna+='A'
    return complementary_dna
