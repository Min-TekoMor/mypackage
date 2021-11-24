from mypackage import myModule

def dna_complementary():
    """
    make sure dna_complementary works correctly
    """

    assert dna_complementary('TCCCGGATCGCATACGAT') == 'AGGGCCTAGCGTATGCTA'
    assert dna_complementary('ATCTTATAATTACCGAGTCGATCGG') == 'TAGAATATTAATGGCTCAGCTAGCC'
    assert dna_complementary('ATCGGACTACGA') == 'TAGCCTGATGCT'