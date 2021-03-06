'''
Function to create a "codon to amino-acid" translation dictionary using a codontable textfile as input
'''

#File used as template (see repository)
codontable = 'codonCodingTable.txt'

def readCodonTable(file):
    with open(file) as f:
        lines = f.read()
        lines = lines.split()
        
        #List of codons on odd lines
        codons = lines[::2]
        #list of residues on even lines
        residues = lines[1::2]
        
        #zip into dictionary with codons as keys and residues as values
        trans_dict = dict(zip(codons, residues))
        
        return trans_dict
