#############################################
# Georgia Doing (doingg@union.edu)
# partner, group:
# 4/8/26
''' HW5 programs, ORF finder'''
#############################################


# turns codon number codNum from seq
def getCodon(seq,codNum):
    return seq[(codNum*3):(codNum*3+3)]

# returns last codon in sequence
def getLastCodon(seq):
    return seq[len(seq)-3:len(seq)]

# returns True if given nucleotide is
# valid, else returns False.
# nt is valid if it's A, T, C, G, or U
def valid_nt(nt):
    if nt=="A" or nt=="T" or\
       nt=="C" or nt=="G" or\
       nt=="U":
        return True
    else:
        return False

# returns True if sequence is valid
# else returns False
def valid_seq(seq):
    for n in range(0,len(seq)):
        if valid_nt(seq[n])==False:
            return False
    return True
    
# 1. Warmup

# returns True if given seq
# starts with "ATG".  Else, returns False
def beginsWithStartCodon(seq):
    first = getCodon(seq,0)
    if first == "ATG":
        return True
    else:
        return False


# returns True if given seq
# ends with a stop codon (TAG, TAA, or TGA).
# Else, returns False
def endsWithStopCodon(sequence):
    last = getLastCodon(sequence)
    if last=="TAG" or last=="TAA" or last=="TGA":
        return True
    else:
        return False


# 2. Mod practice.

# Returns the string "EVEN" if num is an even number
# and "ODD" if it's odd. All even numbers are
# divisible by 2.  All odd numbers are not.
def isEven(num):
    if num%2==0:
        return "EVEN"
    else:
        return "ODD"


# 3. ORF checking.

# given some candidate sequence of nts,
# returns True if candidate is an ORF
# and False if it's not. A candidate is
# an ORF if all of the following are true:
# 1) it's a valid sequence (every nt is legal)
# 2) starts with the start codon
# 3) ends with a stop codon
# 4) length divisible by 3
#    (same reading frame)
def ORF_checker(candidate):
    if beginsWithStartCodon(candidate) and\
       endsWithStopCodon(candidate) and\
       valid_seq(candidate) and\
       len(candidate)%3==0:
        return True
    else:
        return False


# 4. ORF finder.

# returns the first ORF found in NTseq.
# If one is found, print its starting position
# and length before returning it.
# Returns "No ORF" if there are no ORFs in NTseq
def ORF_finder(NTseq):
    for startPos in range(0,len(NTseq)):
        for endPos  in range(startPos+1,len(NTseq)):
            candidate = NTseq[startPos:endPos+1]
            if ORF_checker(candidate)==True:
                print("found ORF at pos " +\
                      str(startPos) +\
                      " with length " +\
                      str(len(candidate)))
                return candidate
    else:
        return "No ORF"


###########################################################
# When you test this, try it out on the big string
# I give you in the main function.  Then go to
#
# http://www.ncbi.nlm.nih.gov/gorf/gorf.html
#
# paste in the same sequence, erase the backslashes,
# and submit it with the "OrfFind" button.
# The first ORF it finds should be the
# same ORF your function finds.  Congrats! You
# just built an actual bioinformatics tool!
###########################################################

def main():
    s = "AGCCTAAGGACCCCAGCCAGCGCCGGTCTAGAGAATTCGGCACGA\
GGCCTCCCTGTATAAGGCAGTGGTCGTAATATGCTTGTGATCGCTCTCTCA\
TCTCGAGGGTCTTCTGAAGCGGCTGGCGCTTTTCATGACACGCACCTCGCGG\
TAAGTTCACCTATCGCAGCATCGACCTGTAGAAGGAGTTCTCCATCGGGCAG\
GCTCTTGATAGTTTGCCCAGTCGCACCCCCTTATCCGATGCCAGTCAGCCCT\
TCTCAGGACTATATCTGCTCTGGAGGCGCGACAAGCCGCGGGATACTTCAAC\
GCAGATTACCACCTCCAGCTCCGCGCACCAGCGCATTCATCCAGCAACCCCG\
CGCGCAAGTTCAACCCACTCTCTGTTCCACGAGCCCTTATCCCAAGAAGATG\
GTCGACGTCAAGCGCCGAGAGAAGGATGCCTTTGCTTCGTCCACTCCTACGA\
ACGAGAAGTTCTGAGATTTTTTTCTGTGATTATCTAGTACGGTCATGCCATT\
GTATTTCTACATCAAAAAAAAAAAAAAAAAAAAA"

    print "Is ATGCCCCTAA an ORF? " + str(ORF_checker("ATGCCCCTAA"))
    print(ORF_finder("AAAATGAATTGA"))
    print(ORF_finder("ATGACAGTGGATGTTTGA"))
    print(ORF_finder(s))

main()








