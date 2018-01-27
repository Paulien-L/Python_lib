codontable = 'codonCodingTable.txt'

def readCodonTable(file):
    with open(file) as f:
        lines = f.read()
        lines = lines.split()
        
        codons = lines[::2]
        residues = lines[1::2]
        
        trans_dict = dict(zip(codons, residues))
        
        return trans_dict