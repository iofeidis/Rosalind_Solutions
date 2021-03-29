def rna_string_number_mod_n(rna_string, n):
    # Even lone RNA_triplets need parentheses, else len(i) == len(str(i))
    rna_codon_table = {
        'A': ('GCU', 'GCC', 'GCA', 'GCG'),
        'C': ('UGU', 'UGC'),
        'D': ('GAU', 'GAC'),
        'E': ('GAA', 'GAG'),
        'F': ('UUU', 'UUC'),
        'G': ('GGU', 'GGC', 'GGA', 'GGG'),
        'H': ('CAU', 'CAC'),
        'I': ('AUU', 'AUC', 'AUA'),
        'K': ('AAA', 'AAG'),
        'L': ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'),
        'M': ('AUG',),
        'N': ('AAU', 'AAC'),
        'P': ('CCU', 'CCC', 'CCA', 'CCG'),
        'Q': ('CAA', 'CAG'),
        'R': ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
        'S': ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'),
        'T': ('ACU', 'ACC', 'ACA', 'ACG'),
        'V': ('GUU', 'GUC', 'GUA', 'GUG'),
        'W': ('UGG',),
        'Y': ('UAU', 'UAC')}
    s = 1
    for i in rna_string:
        s = (s*len(rna_codon_table[i])) % n
    # 3 more for stop codons
    return (s * 3) % n

s1 = "MYCLEHPAISFIIHYLTRYCADISNIATRQQLVRFKNASNPITTDANSVGGGITRTWLDPMQMCDINEPWVICVNMRDDHTVMPMYQRAPLLFMISRIMRNSDGMGYLDFSDMAMEFVIELFMGWMNFQEYKMYKANEECLRHAKTCPYRQAGWPSQISDTGRHDLIVCCGFGHEMMKKLMVFDFTYGYAMCLESRQAVTWIICEQVFDKMNFRWCWTLIWLLHRGIMGKNGMEIDWSDRDDRGNKDFKANERNDQDPPSPTTRTQYNPSVERLYVQKWNDDPGRGVHMFHGKMYHKKCSHNTFRNHENQMACWPWAMKTEFHDHESDVTWWVLNWGIDKSTVWHGAFYVSTMCHTTPWAETHPCCERPLACHLHYENLIEHPTNECCKILAQEAFTSNYGHEFTQRVFIFPMGAGVEIRGQLVNGGARETGRCGDALPRVSAQLQNPPCAKWFNQICPDECGVVEVSFYYHCRGEIATLSNIRKILHHANVNGSVCPYAAAMHWEGLEEMYAMGNLALTVFCYRSKKCAGCYQGAHGSNQRKCKEVGVIKFNCVQYAPIQTYFLSNNWILGEQTQINCGMMEMHHYRKANEHCELGHLLDQMFDALVSYFSNNDEMRKLVKSIDMSKTRGCLFFWYMDLLSHTVDPFDMKQNCRMFTYDTNPVHAMHYHKPSRQVYVYQAGAEFIGEIVLYDTWKNVMSFQPNKFEWFTRQCLKQFVNGYWFWTRQSVVWICNCFGNHNGAKSWPIDETARFAFGSAPFMKRSWAAYWQDFHQRWIWHRARKIPMEGMEDYNHLCAFCPDAPWSVSYSSLKLPIQETQVNHVSCAQNRGKWVYTQCTYRGLVRDISNYQVGKCPIHDDPPRCESDIPRCIVTIAPWPHLFAPFQTNYHCLSLIETHLVERDWIDFKMTRAFEDWRLPPLWFDSFYLEIGAGMQDKEVWDGMPMILYNLQTKHTFTCPMEVVICWREQTTIMLGIHVTVGDEQRSSFHKDEYNRLHLLV"
print(rna_string_number_mod_n(s1, 1000000))