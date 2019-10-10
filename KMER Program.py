#Daanish Fiaz
#KMER HW
import pandas as pd
#Prompting user
file = input("Enter the name of the file: ")
kmerinput = input("Enter the length of the KMER: ")
#kmerinput = 3
kmerinput = int(kmerinput)
#max outcomes
maxpossiblekmers = 4 ** kmerinput

#file = "sequence.fasta"
#First, we have to get the length of the sequence
with open(file, "r") as infile:
    #initialize sequence
    seq = ""
    #for each line in the file
    for line in infile:
        if line.startswith(">"):
            continue
        else:
            seq = seq + line.strip()
            
#This is the correct seqLength
seqLen = len(seq)
#Gives us the length of the sequence, part 1
#Now we have to get the respective nucl frequencies, part two
seqAContent = (seq.upper().count("A") / seqLen)
seqTContent = (seq.upper().count("T") / seqLen)
seqCContent = (seq.upper().count("C") / seqLen)
seqGContent = (seq.upper().count("G") / seqLen)

#Creating loop to find the possible number of kmers
#seqLen
#initialize kmer dictionary to hold the kmer seq and the number of times it shows up in the sequence
kmerdict = {}
for i in range(0, seqLen - kmerinput + 1):
    #set kmer
    kmer = seq[i:i + kmerinput]
    #if kmer is in dict, add 1
    if kmer in kmerdict:
        kmerdict[kmer] += 1
    #if kmer is not in dict, set as 1
    else:
        kmerdict[kmer] = 1
#We have the kmer seqs and observed count, now we have to pull out all of the kmers from the dictionary
kmerseqlist = list(kmerdict.keys())
kmerobservedlist = list(kmerdict.values())
countAList = []
countTList = []
countCList = []
countGList = []
#count the letters for each kmer, multiply counts by their frequencies for the seq
#add all of the counts together after multiplying, then multiply by the length of the sequence
for kmer in kmerseqlist:
    countA = 0
    countT = 0
    countC = 0
    countG = 0
    for letter in kmer:
        if letter == "A":
            countA += 1
        if letter == "T":
            countT += 1
        if letter == "C":
            countC += 1
        if letter == "G":
            countG += 1
    countAList.append(countA)
    countTList.append(countT)
    countCList.append(countC)
    countGList.append(countG)
    #above we have all the lists with the counts of each nucleotide for each kmer
   
#now we want to make a new list with each of the values added from the countA, countT, countC, and countG lists
#the values in this list will be multiplied by their respective frequencies, then added
expectedcounts = []
added = 0
for i in range(0, len(kmerdict)):
    added = (seqAContent ** countAList[i]) * (seqTContent ** countTList[i]) * (seqCContent ** countCList[i]) * (seqGContent ** countGList[i])
    expectedcounts.append(added)
#now we have added counts that has all of the values
for i in range(0, len(kmerdict)):
    #Multiply by the 1/howevermany kmers and the length of the sequence to get expected count of each kmer
    expectedcounts[i] = expectedcounts[i] * seqLen
    #expectedcounts[i] = round(expectedcounts[i])

#Creating chi square value list
#kmerobservedlist holds all of the observed values for each kmer
#expectedcounts holds all of the expected values for each kmer
chiList = []
chisquarevalue = 0
for i in range(0, len(kmerdict)):
    chisquarevalue = (((kmerobservedlist[i] - expectedcounts[i])**2)/expectedcounts[i])
    chiList.append(chisquarevalue)
    chiList[i] = round(chiList[i], 3)
    expectedcounts[i] = round(expectedcounts[i])
#values in chiList match my values as a result of handwritten testing
    
#So lets  organize everything
#kmer sequences are kmerseqlist
#observed count of kmer is kmerobservedlist
#expected count of kmer is expectedcounts
#chisquare list is chiList
df1 = pd.DataFrame(
    {'K-Mer Seq' : kmerseqlist,
     'Observed Count' : kmerobservedlist,
     'Expected Count' : expectedcounts,
     'Chi-Square Value' : chiList
     })
    

#Now the next step is to pull out the top ten according to most frequently occurring observed kmers
#print that out in a table
#The statement below is how to organize the dataframe by top
#Assignment does not specify least to greatest or greatest to least, so I'm assuming least to greatest is fine.
tempdfcounts = (df1.sort_values(by =['Observed Count']))
finaltop10counts = tempdfcounts[-10:]

tempdfchi = (df1.sort_values(by =['Chi-Square Value']))
finaltop10chi = tempdfchi[-10:]

#loop to get the total number of kmers
totalobservedkmers = len(kmerdict)
#Now we have to sort that dictionary to get the top kmers
#Print Statements
print("")
print("The length of the sequence is: " + str(seqLen))
print("")
print("The A nucleotide frequency is: " + str(round(seqAContent, 4)))
print("The T nucleotide frequency is: " + str(round(seqTContent, 4)))
print("The C nucleotide frequency is: " + str(round(seqCContent, 4)))
print("The G nucleotide frequency is: " + str(round(seqGContent, 4)))
print("")
print(str(totalobservedkmers) + " of " + str(maxpossiblekmers) + " possible " + str(kmerinput) + "-mers found.")
print("")
print("Top 10 Observed Counts")
#print final top 10 counts for observed values
print(finaltop10counts.to_string(index = False))
#gap print
print("")
print("Top 10 Chi-Square Values")
#print final top 10 chi square values
print(finaltop10chi.to_string(index = False))
