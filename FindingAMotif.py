def returnMotif(s, t):
    pos = []
    for i in range(len(s)-len(t)):
        if s[i:i+len(t):] == t:
            pos.append(i+1)
    return pos

print(returnMotif('GATATATGCATATACTT', 'ATAT'))