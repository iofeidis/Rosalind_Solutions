def fasta_dict(filepath):
    # with open(filepath) as f:
    #     s = f.read().replace('\n', '').split('>')[1::]
    #     # print(s)
    #     d = {}
    #     for i in s:
    #         d.setdefault(i[:13:], i[13::])
    #     # print(d)
    #     return d
    with open(filepath) as f:
        # Read Line by Line
        lines = f.readlines()
        vals = []
        keys = []
        st = []
        for s in lines:
            if s[0] != '>':
                st.append(s.replace('\n', ''))
            else:
                keys.append(s[1::].replace('\n', ''))
                vals.append("".join(st))
                st = []
        vals.append("".join(st))
        vals = vals[1::]
        # print(vals)
        d = {}
        for i, j in zip(keys, vals):
            d.update({i: j})
        # print(d)
        return d

# print(fasta_dict("Datasets/rosalind_lcsm.txt"))
