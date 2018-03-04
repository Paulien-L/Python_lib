'''
Functions to parse a PBD file and analyze the protein's residues and the hetero atoms in the crystal structure.
Protein used: 5kkk, sperm whale myoglobin.
Author: Paulien L
Date: 13-12-2017
Note: results won't be entirely correct as A/B variants of residues in the PDB file are ignored.
'''

#Specify your own file path here
input = r'5kkk.pdb'

'''
Parses PDB file to store information about central carbon (CA) atoms and heterogen atoms (HETATM) in a dictionary.
Information stored about CA atoms: number (self-given index for the dictionary), residue, index from the PDB file,
and the x-y-z coordinates of each atom.
input = PDB file to be parsed
'''
def parsePDB(input):
    returnData = {
        'ATOM': [],
        'HETATM': []
        }
    count = 0
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            if 'ATOM' and 'CA' in words:
                count += 1
                data = {
                "number" : count,
                "residue" : words[3],
                "index" : words[5],
                "xcoord" : words[6],
                "ycoord" : words[7],
                "zcoord" : words[8]
                }
                
                returnData['ATOM'].append(data)
                    
            if 'HETATM' in words:
                heterogen = words
                returnData['HETATM'].append(words)
        return returnData

'''
Prints parsed information of the PDB file.
'''
def printPDB():
    data = parsePDB(input)
    for item in data['ATOM']:
        print('Residue: ' + str(item['residue']) + ' ' +'Position: ' + str(item['xcoord']) + ' ' + str(item['ycoord']) + ' ' + str(item['zcoord']) + ' ')
    for item in data['HETATM']:
        print(item)


'''
Merges two dictionaries based on a common key.
l1 = list1 or dictionary1
l2 = list2 or dictionary2
key = common key
'''
def merge_lists(l1, l2, key):
    merged = {}
    for item in l1+l2:
        if item[key] in merged:
            merged[item[key]].update(item)
        else:
            merged[item[key]] = item
    return merged.values()

import math

'''
Determines the Euclidean distance to the center of the protein for each central carbon atom in the parsed ATOM data.
These distances and a self-given index are put in a dictionary. This dictionary is then merged with the existing
dictionary from the parsePDB function.
'''
def distance2Center():
    data = parsePDB(input)
    valueList = list(data.values())
    n = len(valueList[0])
    atomData = data['ATOM']
    
    xposList = []
    yposList = []
    zposList = []
    posList = []
    
    for item in atomData:
        xpos = float(item['xcoord'])
        ypos = float(item['ycoord'])
        zpos = float(item['zcoord'])
        
        pos = [xpos, ypos, zpos]
        posList.append(pos)
        
        xposList.append(xpos)
        yposList.append(ypos)
        zposList.append(zpos)
    
    avgX = sum(xposList)/n
    avgY = sum(yposList)/n
    avgZ = sum(zposList)/n
    
    distance = []
    counter = 0
    for pos in posList:
        counter += 1
        dist = {
            'number' : counter,
            'distance' : math.sqrt(((avgX - pos[0])**2) + ((avgY - pos[1])**2) + ((avgZ - pos[2])**2))
            }
        distance.append(dist)
    
    result = merge_lists(atomData, distance, 'number')
    return result

'''
Divides data from distance2Center function into hydrophobic or hydrophilic residues to analyze where most
hydrophobic/hydrophilic residues are relative to the center of the protein.
'''
def hydrophobic():
    hydroData = distance2Center()
    hydroData = list(hydroData)
    hydrophobic = ['ALA', 'CYS', 'PHE', 'ILE', 'LEU', 'MET', 'PRO', 'AVAL', 'BVAL' , 'VAL', 'TRP']
    for item in hydroData:
        if item['residue'] in hydrophobic:
            item['hydrophobic'] = 1
        else:
            item['hydrophobic'] = 0
    return hydroData

import sys

'''
Provides output as text file with the residue, distance to center for the CA atoms 
and whether the residue is hydrophobic or hydrophilic.
'''   
def output():
    outputData = hydrophobic()
	#Specify your own file path here
    sys.stdout = open(r'output.txt', "w")
    for item in outputData:
        print((str(item['residue']) + ' ' + str(item['distance']) + ' ' + str(item['hydrophobic'])))
    
'''
Returns the x-y-z position of the inputted heterogen based on the PDB file.
heterogen = hetrogen of interest
'''
def searchHeterogen(heterogen):
    data = parsePDB(input)
    heterogenposition = []
    for item in data['HETATM']:
        if item[2] == heterogen:
            hetposX = float(item[6])
            hetposY = float(item[7])
            hetposZ = float(item[8])
            hetpos = [hetposX, hetposY, hetposZ]
            heterogenposition.append(hetpos)
            
    return heterogenposition

'''
Calculates distance between CA atoms in the protein and the iron heterogen from the haem group (for this protein)
'''	
def distance2FE():
    data = parsePDB(input)
    atomData = data['ATOM']
    FePosition = searchHeterogen('FE')
    FePosX = 0
    FePosY = 0
    FePosZ = 0
    posList = []
    FeDistance = []
    
    
    for pos in FePosition:
        FePosX = pos[0]
        FePosY = pos[1]
        FePosZ = pos[2]
    
    for item in atomData:
        xpos = float(item['xcoord'])
        ypos = float(item['ycoord'])
        zpos = float(item['zcoord'])
        
        pos = [xpos, ypos, zpos]
        posList.append(pos)
    
    for pos in posList:
        Fedist = [math.sqrt(((FePosX - pos[0])**2) + ((FePosY - pos[1])**2) + ((FePosZ - pos[2])**2))]
        FeDistance.append(Fedist)
    
    return FeDistance

'''
Prints the five CA residues in the ATOM data closest to the iron heterogen.
'''
def closestFive():
    data = parsePDB(input)
    atomData = data['ATOM']
    FeDistance = distance2FE()
    
    atomList = []
    for item in atomData:
        atmlist = list(item.values())
        atomList.append(atmlist)
    
    resultList = []
    for x,y in zip(atomList, FeDistance):
        result = [x[1], x[2], x[3], x[4], x[5], y[0]]
        resultList.append(result)
    sortedResult = sorted(resultList, key=lambda item: item[5])
    closestFive = sortedResult[0:5]
    for i in closestFive:
        print(i)
