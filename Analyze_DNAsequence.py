'''
Functions to analyse a sequence's relative base frequency, melting temperature and codon frequencies
Created on Jan 27, 2018

@author: Paulien L
'''

'''
Determines relative frequencies of bases in a DNA sequence.
seq = sequence to be analysed
'''
def freq(seq):
    seq = seq.upper()
    freq_A = seq.count('A')/len(seq)
    freq_T = seq.count('T')/len(seq)
    freq_C = seq.count('C')/len(seq)
    freq_G = seq.count('G')/len(seq)

    print("relative frequency A: " + (str)(freq_A))
    print("relative frequency T: " + (str)(freq_T))
    print("relative frequency C: " + (str)(freq_C))
    print("relative frequency G: " + (str)(freq_G))

'''
Calculates melting temperature of given sequence.
If sequence length < 14, formula Tm= 4*Nstrong+ 2*Nweak is used,
else formula Tm = 64.9+ 41(Nstrong - 16.4)/Ntotal is used.
seq = sequence to be analysed
'''
def meltingTemp(seq):
    seq = seq.upper()
    nb_weak = (seq.count('A')) + (seq.count('T'))
    nb_strong = (seq.count('C')) + (seq.count('G'))
    nb_total = nb_strong + nb_weak
    
    if len(seq) < 14:
        melting_temp = (4*nb_strong) + (2*nb_weak)
    else:
        melting_temp = 64.9 + ((41*(nb_strong - 16.4))/nb_total)
    
    print('Melting temperature: ' + (str)(melting_temp) + ' degrees Celcius')

'''
Generates a list of all codons and saves them in a dictionary
'''
base_list = list("atgc")
codon_list = [a+b+c for a in base_list for b in base_list for c in base_list]
codon_dict = {codon:0 for codon in codon_list}

'''
Determines frequencies of codons in the given sequence
seq = sequence to be analysed
'''
def codonfreq(seq):
    for i in range(0, len(seq), 3):
        codon_dict[seq[i:i+3]] += 1
    print(codon_dict)
