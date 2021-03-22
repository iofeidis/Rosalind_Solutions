with open("Datasets/rosalind_cons.txt") as f:
    # Read Line by Line
    lines = f.readlines()
    dna = []
    st = []
    for s in lines:
        if s[0] != '>':
            st.append(s.replace('\n', ''))
        else:
            dna.append("".join(st))
            st = []
    dna.append("".join(st))
    dna = dna[1::]
    dna = [["".join(dna[j][i]) for j in range(len(dna))] for i in range(len(dna[0]))]
    l = []
    for i in dna:
        l.append("".join([str(k) for k in i]))
    # print(l)
    d = {}
    d.setdefault('A', [])
    d.setdefault('C', [])
    d.setdefault('G', [])
    d.setdefault('T', [])
    for s in dna:
        # print(s)
        d['A'].append(s.count('A'))
        d['C'].append(s.count('C'))
        d['G'].append(s.count('G'))
        d['T'].append(s.count('T'))
    mx = [i for i in d.values()]
    c = []
    for i in range(len(mx[1])):
        maax = d['A'][i]
        mk = 'A'
        for k in d.keys():
            if d[k][i] > maax:
                maax = d[k][i]
                mk = k
        c.append(mk)
    # DEBUG
    # print("Length of mx[1]: ", len(mx[1]))
    print("".join(c))
    # print("Length of consensus: ", len(c))
    # print("Length of A, C, G, T: ", len(dna))

    for k, v in d.items():
        print(str(k) + ': ' + ' '.join([str(i) for i in v]))

