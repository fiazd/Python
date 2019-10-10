#Daanish NW Program
#Worked with Owais on constructing matrix
#make SeqIO available as well as numpy
from Bio import SeqIO
import numpy as np

#initialize strings to hold file names
seq1name = input('Input file name 1: ')
#seq1name = 'Sample.fasta'
#Get a list to put the two sequences in
seqlist = []

#loop through sequences in the file given by the user
for seq_record in SeqIO.parse(seq1name, 'fasta'):
    #add sequence to list
    seqlist.append(str(seq_record.seq))
    

#Join the two items in the list to two different strings and capitalize those strings just in case it's in lower case
seq1 = ''.join(seqlist[0])
seq1.upper()
seq2 = ''.join(seqlist[1])
seq2.upper()

#seq1 = 'ATGAAGGC'
#seq2 = 'GGTAAGGC'
seq1length = len(seq1)
seq2length = len(seq2)
#match = 1
#mismatch = -1
#gap = -2
#Have the user input each of the match mismatch and gap values
match = input('Input match score value: ')
mismatch = input('Input mismatch score value: ')
gap = input('Input gap score value: ')
#convert the values just to make sure
match = int(match)
mismatch = int(mismatch)
gap = int(gap)

#Creating the first matrix (m1), increment by gap score starting from after zero
#create scoredict to store the values associated so we can access them
scoredict = {'match' : match, 'mismatch' : mismatch, 'gap' : gap}
#We do plus one to start with zero in the array this creates the zero matrix based upon what the length of the sequences are
m1 = np.zeros((seq1length + 1, seq2length + 1))

#now we have to fill the "headers" with the incremented values
for i in range(seq1length + 1):
    m1[i][0] = scoredict['gap'] * i
for j in range(seq2length + 1):
    m1[0][j] = scoredict['gap'] * j

#now, we have to fill in the matrix
bestscorelist = []
for i in range(1, seq1length + 1):
    for j in range(1, seq2length + 1):
        #match
        if seq1[i-1] == seq2[j-1]:
            score1 = m1[i-1][j-1] + scoredict['match']
        #mistmatch
        else:
            score1 = m1[i-1][j-1] + scoredict['mismatch']
        score2 = m1[i][j-1] + scoredict['gap']
        score3 = m1[i-1][j] + scoredict['gap']
        m1[i,j] = max(score1, score2, score3)
        #append all of the scores, then print out the last one, which will be the best
        bestscorelist.append(max(score1, score2, score3))
finalscore = bestscorelist[-1]
#new strings with alignment sequences
alignseq1 = ''
alignseq2 = ''

i = len(seq1)
j = len(seq2)

    
#while BOTH i and j are bigger than zero
while i > 0 and j > 0:
    #all the different values will help us keep the loop simple and prevent mistakes in coding
    currscore = m1[i][j]
    topleftscore = m1[i-1][j-1]
    leftscore = m1[i-1][j]
    upperscore = m1[i][j-1]
    #we need to figure out where the current score was pulled from, so if currscore is equal to that value
    #add that to the alignseq and decrement i or j depending upon where the score was pulled from.
    #you have to add gap because we got the difference and now it's reversed.
    #leftbound
    #using this to check the value of the topleft before the traceback loop
    #this varies based upon different conditions
    #if it matches
    if seq1[i-1] == seq2[j-1]:
        valueholder = match
    #if it is a mismatch
    elif seq1[i-1] != seq2[j-1]:
        valueholder = mismatch
    #if it is a gap
    elif seq1[i-1] == '-' or seq2[j-1] == '-':
        valueholder = gap
    if currscore == leftscore + scoredict['gap']:
        alignseq2 += seq2[j-1]
        alignseq1 += '-'
        i -= 1
    #upperbound    
    elif currscore == upperscore + scoredict['gap']:
        alignseq1 += seq1[i-1]
        alignseq2 += '-'
        j -= 1
    #topleftbound
    elif currscore == topleftscore + valueholder:
        alignseq1 += seq1[i-1]
        alignseq2 += seq2[j-1]
        i -= 1
        j -= 1
#for some reason it's not reaching all the way back to the beginning
#So one of them reached zero, but which one? so we have to tell it to keep going exclusively and keep appending
while j > 0:
    alignseq1 += seq1[i-1]
    alignseq2 += '-'
    j -= 1
while i > 0:
    alignseq2 += seq2[j-1]
    alignseq1 += '-'
    i -=1
#now i have to reverse the sequences this is done by [::-1]
#but now i have to finish the statements allowing the user to input the given sequence.
#move all the print statements to the bottom for consistency
print('Score: ' + str(int(finalscore)))
print(alignseq1[::-1])
print(alignseq2[::-1])

        
