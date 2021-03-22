import re


# Read Proteins from Dataset and Pass their .fasta to .txt file
def file_manipulation1():
    # Get Protein Names
    with open(file="Datasets/protein_names.txt") as f:
        lines = f.readlines()
    # Convert Protein Names to URLs
    lines2 = ["https://www.uniprot.org/uniprot/" + i.replace('\n', '') + ".fasta\n"
              for i in lines]
    # print(lines2)
    # Write URLs to .txt
    with open(file="Datasets/tobedown.txt", mode='w') as f:
        f.writelines(lines2)
    # print([i.replace('\n', '') for i in lines])
    return


def check_protein_motif(filepath):
    rex = "(?=[N][^P][ST][^P])"
    with open(filepath) as f:
        # Read Line by Line
        lines = f.readlines()
        vals, keys, st = [], [], []
        for s in lines:
            if s[0] != '>':
                st.append(s.replace('\n', ''))
            else:
                keys.append(s.split('|')[1])
                vals.append("".join(st))
                st = []
        vals.append("".join(st))
        vals = vals[1::]
        d = {}
        for i, j in zip(keys, vals):
            d.update({i: j})
        # print(d)
    with open(file="Datasets/protein_names.txt") as f:
        lines = f.readlines()
    lines = [i.replace('\n', '') for i in lines]
    for (k, j) in zip(d.keys(), lines):
        print(j)
        pos = [i.start() for i in re.finditer(rex, d[k])]
        print(' '.join([str(i + 1) for i in pos]))
