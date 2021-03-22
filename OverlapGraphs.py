# def overlap_graphs("Datasets/rosalind_cons.txt"):
with open("Datasets/rosalind_grph.txt") as f:
    s = f.read().replace('\n', '').split('>')[1::]
    # print(s)
    d = {}
    for i in s:
        d.setdefault(i[:13:], i[13::])
    print(d)
    se = set()
    for i in d.keys():
        for j in d.keys():
            if i != j:
                k1, k2 = d[i][:3:], d[j][len(d[j])-3:len(d[j]):]
                if k1 == k2:
                    se.add(j + ' ' + i)
                # print(i, j)
                # print(i, k1, j, k2)
    for i in se:
        print(i)

