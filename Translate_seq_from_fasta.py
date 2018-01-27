sequence = r'C:\Users\Computer\Documents\Bioinformatics phase 1\Semester 1\Practical computing\sequence.fasta'
def readSeq(file):
    with open(file) as f:
        f.readline()
        lines = f.readlines()
        data = []
        for line in lines:
            line = line.rstrip()
            data.append(line)
        seq = ''.join(data)
        return seq

def getCodons(seq, start):
    seq = seq.lower()
    result = []
    stop = ['taa', 'tga', 'tag']
    
    while (start+3) <= len(seq):
        codon = seq[start:(start+3)]
        result.append(codon)
        if codon in stop:
            start = len(seq)
        else:
            start += 3
    return result

# translate the coding sequence
def translate(table, seq):
    result = ''
    for codon in getCodons(seq, 0):
        result += table[codon]
    return result