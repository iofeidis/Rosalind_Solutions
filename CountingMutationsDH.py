with open('Datasets/rosalind_hamm.txt') as f:
    lines = f.readlines()
    print(lines)
    # lines = ['GAGCCTACTAACGGGATA', 'CATCGTAATGACGGCCTT']
    p = 0
    for i in range(len(lines[0])):
        if lines[0][i] != lines[1][i]:
            p += 1
    print(p)