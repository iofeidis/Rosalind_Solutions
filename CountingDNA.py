s = GCTGAAAGTTTATTCTTCAGTTTGTTGGTTAAGTCTGGGCATGCGGCTTTAGGCCGCAGGGATCGTTCAATTCCCCCACGTTATTTCGACCGTCTAGGCTACCTGGGTCGGGCCGTGTAGCGCCCTGCTTTTCTTTAGCTCTCCGTAAAGCCGATGAGGGGTACAACTTGCTGTGGTGGTGTCCCATGACGGATCGTTTACTTGGTTGGGGGGATCACGTACATTAGGGGCGCGAGCCTGCTTTACGTAGATTGGGCATCGAATACGGGCTCTAGCAGAACGAAAGAGGTGCGCGTCCTCGCCTTATGAGTATGCAATCTCCCCCATGAGATGGCCTTACCGTTTGATGTGGACTGTAGAGTGCCGATGGGAGTGGCGGGCCTCGGAAGCATATCACGGCACAGGTCGTTATGCGGTGTTGAGTTTTTTTCCAATCGCGACAACCGAGATGTAAATGAGTAGCCTCCGCAGAACGCTGTAAGATTTATGTTAGGCTTCAAGATTGGGGCGTTACCCTAGGATCCGCACCATCAGGTTATATGCCATGAATGACGAACTTCTCCAACCTGTGGTGCCGTGCATAACCGTATATTTCCAGTTATACCGCTTAAGCTGCCCGGTGGCCCTGCCGTACACGTCGTCGCCGATGAGACTCTATGAAATGACCGTATTCGTTTGTGTCGTCATCAGTCAGCTTTTACCTAGGACTACTTTTTCGCGACACGCATATTCGCCAGAATCTCTTTCTCCCCATAGAAACCGCGATCTACGCCGATACACCCAAACGTGATTAGTGTAATCAGTATAGCCCGTACGGAATTGTATCAATAATGTGTCATCCGGGCAGATAGGAAGCAACAGTAGACCATTGAGTAACCAATGTAAACACTAACCCCCTGTGAGACTCATCGCTCACTATTCAAGAGACTACATAGCAGCCCAGCTCCACTATACCGGACATACGCCACTATGTGCCCACAAGACAAACA
def countingDNA(s):
    return s.count('A'), s.count('C'), s.count('G'), s.count('T') 