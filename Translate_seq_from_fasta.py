'''
Set of functions to read a DNA sequence from a fasta file and translate it to a sequence of amino-acids.
'''

#Sequence to translate (specify your own path)
sequence = 'sequence.fasta'

'''
Function to read the sequence from the fasta file
'''
def readSeq(file):
    with open(file) as f:
        #Reads header of file
        f.readline()
        #Reads body of file
        lines = f.readlines()
        data = []
        for line in lines:
            #Strips \n at end of lines
            line = line.rstrip()
            data.append(line)
        
        #Joins lines together into one string
        seq = ''.join(data)
        return seq

'''
Function to retrieve the codons of a sequence.
seq = sequence to find codons of
start = start of the open reading frame
'''
def getCodons(seq, start):
    #Sets given sequence to lowercase letters
    seq = seq.lower()
    result = []
    
    #Defines stop codons
    stop = ['taa', 'tga', 'tag']
    
    #Loops as long as there are three bases from the end (so there's still a codon left)
    while (start+3) <= len(seq):
        #Defines codon as three bases
        codon = seq[start:(start+3)]
        result.append(codon)
        
        #Stops while-loop if a stop codon is encountered
        if codon in stop:
            start = len(seq)
        #Adds three steps to starting point to start at next codon
        else:
            start += 3
    return result

'''
Function to translate a DNA-sequence to an amino-acid sequence based on a codon table.
table = codon table used
seq = sequence to be translated
start = start of the open reading frame
'''
def translate(table, seq, start):
    result = ''
    for codon in getCodons(seq, start):
        result += table[codon]
    return result
