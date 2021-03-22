import Fasta2Dict


def finding_shared_motif(filepath):
    d = Fasta2Dict.fasta_dict(filepath)
    print(d)
    # DNA string with min length
    smin = min(d.values(), key=len)
    for i in reversed(range(len(smin) - 1)):
        for j in range(len(smin) - i + 1):
            t = smin[j:j + i:]
            flag = True
            for v in d.values():
                if t not in v:
                    flag = False
                    break
            if flag:
                print(t)
                return


finding_shared_motif("Datasets/rosalind_lcsm.txt")
