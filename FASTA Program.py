#Daanish Fiaz FASTA program
#Open the file 
filename = '1_SampleData.fasta'
fh = open(filename, "r")

#Initialize a whole bunch of stuff
headerlist = []
seqlist = []
iseq = ''
eachseq = ''

#Print table header has to be 20 to let gc print properly
print('{:>21} {:>20} {:>20}'.format('Accession Number','Length of Sequence', 'GC Content'))

seq = ""
for line in fh:
    #Removes /n
    line = line.strip()
    #Extract the headerline
    if '>' in line:
        #Splits line by | so we can index
        splitline = line.split('|')
        #splitline 3 is the accession number
        anumber = splitline[3]
        #len headerlist will let us calc average seq length and 
        headerlist.append(splitline[3])
        #this is skipped for the first time it hits the carrot 
        if seq != '':
            seqlist.append(seq)
        #resets it so we don't keep appending
        seq = ""
    else:
        
        iseq = ''.join(seqlist)
        total_len = len(iseq) / len(headerlist)
        seq += line
                

#this appends the last one
seqlist.append(seq)

#Loop that will get the len
lengthlist = []
gclist = []
A2 = 0
T2 = 0
C2 = 0
G2 = 0
for item in seqlist:
    #adds this to a list so we can print it out
    lengthlist.append(len(item))
    for letter in item:
        if letter == 'A':
            A2 += 1
        if letter == 'T':
            T2 += 1
        if letter == 'C':
            C2 += 1
        if letter == 'G':
            G2 += 1
    #gc average for each sequence
    total_gc2 = ((G2 + C2) / (A2 + T2 + C2 + G2)) / (len(headerlist))
    #adds to a list so we can print it out
    gclist.append(total_gc2)
    
#Append each sequence to a string, then append that string to a list.
#Calculate average GC Content for entire sequence
A = 0
T = 0
C = 0
G = 0
for letter in iseq:
    if letter == 'A':
        A += 1
    if letter == 'T':
        T += 1
    if letter == 'C':
        C += 1
    if letter == 'G':
        G += 1
#total gc average
total_gc = ((G + C) / (A + T + C + G)) / (len(headerlist))

#increments to print out everything
x = 0
for i in headerlist:
    print('{:>21} {:>20} {:>20}'.format(headerlist[x], lengthlist[x], gclist[x])) 
    x += 1

#Prints everything out
print('Total number of sequences is ' + str(len(headerlist)) + '.')
print('Total average length of each sequence is ' + str(total_len) + '.')
print('Total average GC content for each sequence is ' + str(total_gc) + '.')
      
      
      
      
