with open('Datasets/rosalind_gc.txt') as f:
    lines = f.readlines()
    # print(lines.split('>')[1])
    # print(lines)
    d = {}
    for s in lines:
        if s[0] == '>':
            key = s[1:14:]
            d.setdefault(key, '')
        else:
            d.update({key: str(d[key] + s).replace('\n', '')})

    d2 = {}
    for k in d.keys():
        content = ((d[k].count('G') + d[k].count('C')) / len(d[k]))
        d2.update({k: content})

    for k in d2.keys():
        if d2[k] == max(d2.values()):
            print(k + ' ' + str(round(d2[k]*100, 4))[:9:])

    # print(d2.values())