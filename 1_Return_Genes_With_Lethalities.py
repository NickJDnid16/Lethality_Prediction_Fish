'''
Created on 23 Oct 2015

@author: nid16
'''

import codecs
from itertools import repeat
import csv
import sys
inputfile = open('./phenoGeneCleanData_fish_2016.02.19.txt', mode='rb')
outputfile = open('./Gene&Lethality_Rows.txt', mode='wb')
PhenLines = []
for line in inputfile:
    if "ZDB" in line:
        PhenLines.append(line)

inputfile.close()




input = csv.reader(PhenLines, delimiter='\t')
outputfile = csv.writer(outputfile)

for row in input:

    count = int (1)


    if count > 0:

        outputfile.writerows(repeat(row[1:2] + row[10:11], count))

        print row[1] + row[10]

data = {}

inputfile = open('./Gene&Lethality_Rows.txt', mode='rb')
outputfile = open('./Genes_With_All_Lethality.txt', mode='wb')

for line in inputfile:
    split_string = line.split(",")
    genome = split_string [0]
    lethalNotation = split_string [1]
    l = ",lethal" in line
    d = ",dead" in line
    v = ",viable" in line
    a = ",alive" in line
    if not (l or  d or v or a):
        lethalNotation = "other"
    if a:
        lethalNotation = "viable"
    if d :
        lethalNotation = "lethal"

    data [genome] = data.get(genome,"")+lethalNotation.rstrip('\r\n')+","


for x in data:

    outputfile.write(x+","+data[x]+"\n")

outputfile.close()



########################################

#sys.exit("STOPPED")



outputfile = open('./Single_Lethality_Genes.txt', mode='wb')
inputfile = open('./Genes_With_All_Lethality.txt', mode='rb')
essOutputfile = open('./Lethal_Fish.txt', mode='wb')
for line in inputfile:

    l = ",lethal" in line
    o = ",other" in line
    v = ",viable" in line



    if ((l) and (v)):
        print ("Ignoring Line")
    ##elif (d and v or vv):
        ##print ("Ignoring Line")
    else:
        line = line.rstrip()
        bits = line.split(',')
        if((v) or (o) and (not l)):
            bit = bits[0]+",viable\n"
            print (bit)
            outputfile.write(bit)
        elif((l) and (o)):
            bit = bits[0]+",lethal\n"
            print (bit)
            outputfile.write(bit)
            essOutputfile.write(bits[0] + "\n")
        elif((not l) and (not v)):
            bit = bits[0]+",lethal\n"
            print (bit)
            outputfile.write(bit)
            essOutputfile.write(bits[0] + "\n")
        elif ((not l) and (not v) and (not o)):

            print("Not Viable OR Lethal")


outputfile.close()


############################################################################################


