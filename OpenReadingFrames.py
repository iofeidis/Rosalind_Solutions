import Fasta2Dict


def orfs(filepath):
    d = Fasta2Dict.fasta_dict(filepath)
    # Only the first string (same as max in this situation)
    dna = max(d.values())
    dna_codons = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }
    stop_codons = ('TAG', 'TGA', 'TAA')
    orfslist = set()
    # The original string and its complement reversed
    dna_s = [dna, dna[::-1].replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()]
    # 2 strings
    for s in dna_s:
        # 3 ways of reading the frame
        for p in range(2):
            for i in range(p, len(s) - 2 + p):
                if s[i:i+3:] == 'ATG':
                    sk = s[i::]
                    for j in range(0, len(sk) - 2, 3):
                        if sk[j:j+3:] in stop_codons:
                            stop = j
                            # print(sk[:stop + 3:])
                            orfslist.add(sk[:stop + 3:])
                            break
    orfsset = set()
    # Remove duplicates
    for k in orfslist:
        orfsset.add("".join([dna_codons[k[i:i+3:]] for i in range(0, len(k) - 2, 3)]).replace('_', ''))
    # Print them as requested
    for i in orfsset:
        print(i)


orfs("Datasets/rosalind_orf.txt")
