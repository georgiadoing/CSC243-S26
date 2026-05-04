# don't forget your header


# turns codon number codNum from seq
def getCodon(seq,codNum):
    return seq[(codNum*3):(codNum*3+3)]

# returns last codon in sequence
def getLastCodon(seq):
    return seq[len(seq)-3:len(seq)]

# returns True if sequence is valid
# else returns False
def valid_seq(seq):
    for n in range(0,len(seq)):
        if valid_nt(seq[n])==False:
            return False
    return True
    
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

# 1. Warmup
# Write the following two functions.
# They should neither print anything
# nor should they access substrings
# directly (no [ or ] in your code).
# Instead call other functions and
# use their return values.  Test
# and print in main() to make sure they work.

# returns True if given seq
# starts with "ATG".  Else, returns
# False
#def beginsWithStartCodon(seq):





# returns True if given seq
# ends with a stop codon (TAG, TAA, or TGA).
# Else, returns False.
# Using other functions will make this
# function a LOT easier to write than
# your pseudocode from Homework 1!
#def endsWithStopCodon(sequence):





# All codons in an ORF must be in the same
# reading frame.  For example, in "CCGTATA"
# CCG and ATA are not in the same frame.
# We can guarantee that we have a single
# reading frame with no "leftover" nts
# by making sure the total number of
# nucleotides is divisible by 3. How do we
# do that? With a new operator.  We already have
# +, -, *, and /.  The new one is %, which
# stands for *modulo*.  9%2 is read
# "nine mod two" and means the remainder
# you get after doing 9/2 in long division.
# Since 2 goes into 9 four times, (2*4 = 8)
# it leaves a remainder of 1.  So 9%2 equals 1.
# This gives an easy way of finding divisibility.
# If x%4 leaves no remainder, then you know
# x is divisible by 4.  Example: if x is 20,
# 20%4 equals 0, so you know 4 goes into 20
# evenly.

# 2. Mod practice.
# Write and test the following:

# Returns the string "EVEN" if num is an even number
# and "ODD" if it's odd. All even numbers are
# divisible by 2.  All odd numbers are not.
#def isEven(num):





# 3. ORF checking.
# You're now ready to
# take a sequence and determine
# if it's an ORF or not. Write the following.
# Again, using substrings is disallowed.
# Use your other functions to make this easy.

# given some candidate sequence of nts,
# returns True if candidate is an ORF
# and False if it's not. A candidate is
# an ORF if all of the following are true:
# 1) it's a valid sequence (every nt is legal)
# 2) starts with the start codon
# 3) ends with a stop codon
# 4) length divisible by 3
#    (same reading frame)
# Test this one thoroughly!
#def ORF_checker(candidate):





# Almost there!  The real ORF finder doesn't just
# see if what you give it is an ORF or not.  It
# takes any old nt sequence and finds ORFs *within* it.
# So if you give it "CGACTAGTATGAGGTATGGACGGCCTTAACCC"
# ORF finder will find the 21-base ORF
# "ATGAGGTATGGACGGCCTTAA" starting at position 8 in
# the big string.  (The real ORF finder won't work
# on this small example because it's just that - too small.
# But you get the idea.)
#
# To do this, we'll use the ORF_checker you just wrote
# to check EVERY POSSIBLE SUBSTRING in the big string.
# In other words, for the example above, we will check
# C
# CG
# CGA
# CGAC
# CGACT
# etc. to see if any of them are ORFs. That takes
# care of all sequences that start at position 0.
# Now we need to check all substrings starting
# at position 1:
# G
# GA
# GAC
# GACT
# GACTA
# etc.  And then we need to check all substrings
# that start at position 2, and then 3, then 4, etc.
# So we need two variables: one to keep track
# of our starting position and one to keep track
# of the ending position.  And we'll check every
# possible combination of starting and ending
# positions.  This is a job for a nested loop.
# Here's the pseudocode for ORF_finder:
#
# for every possible starting position
#    for every possible ending position
#        determine the substring that starts\
#        and ends at the specified positions
#        
#        see if that substring is an ORF
#
#        if so
#           print its length and start position
#           return the ORF
#
#

# 4. ORF finder.
# You're ready.  Write the function.  You may
# use any Python you like, including substrings.
# Call on other functions to make your job easier.
#
# returns the first ORF found in NTseq.
# If one is found, print its starting position
# and length before returning it.
# Returns "No ORF" if there are no ORFs in NTseq
#def ORF_finder(NTseq):






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

main()








