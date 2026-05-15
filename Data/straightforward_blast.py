#############################################
# Georgia Doing (doingg@union.edu)
# partner, group:
# 4/8/26
''' HW4 programs, straightforward blast'''
#############################################

'''
BLAST works by padding "blanks" to the shorter sequence to indicate places where mutations occurred; that is, where insertions or deletions of sets of amino acids took place. A pairwise alignment of each position is then done, with points being given for a matching position and fewer points given (or even points taken away!) for a mismatching position. For example, we might give 1 point for an exact match and 0 points for a mismatch. For the example above, we would get a final score of 3 points: 1 each for the first column (S), the fourth column (Y), and the fifth column (R). The mismatch (G with R) or matches involving a blank would not score any points. 

It's now time to write the alignment matcher. The straightforward algorithm we'll be using is to try every possible combination of where the "blanks" could be in the shorter sequence. We'll find all the scores of all of the possibilities, and the biggest one will be our best hit. 

# intractable O(n!) way of doing alignment matching
'''



# add this if nucleotides match
MATCH_SCORE = 1  
# add this if nucleotides don't match
MISMATCH_SCORE = 0  
# True to turn on debugging
DEBUG = False    

# make first string have all gaps (dashes) and be the same length as second
def pad_with_gaps(second):
    first=""
    for m in range(0,len(second)):
        first = first + "-"
    return first

# make a new string by replacing someString[position] with letter
def replace(someString, position, letter):
    return someString[0:position] + letter + someString[position+1:len(someString)]

# given two equal-length strings, figure out score and return it
def find_score(first,second):
    score=0
    for i in range(0,len(first)):
        if first[i]==second[i]:
            score=score+MATCH_SCORE
        else:
            score=score+MISMATCH_SCORE
    return score

# finds the alignment in a dumb way -- tries every combo assuming that
# string one has length 3 (so 3 nested for loops)
def find_alignment(shorter,longer):
    first = ""
    maxScore = 0

    for i in range(0,len(longer)):
        for j in range(i+1,len(longer)):
            for k in range(j+1,len(longer)):
                first = pad_with_gaps(longer)
                first=replace(first,i,shorter[0])               
                first=replace(first,j,shorter[1])
                first=replace(first,k,shorter[2])
                currentScore = find_score(first,longer)
                if currentScore > maxScore:
                    maxScore = currentScore
                    finalFirst = first
                if DEBUG:
                    print(first)
                    print(longer)
                    print(currentScore)

    print("Best score is", maxScore)
    print(finalFirst)
    print(longer)
   
############ end of primary functions #############

# main starts here; len(two) will always be >= len(one)
#one = "ACT"
#two = "ACAGTCGAATGCATAAGCGGAGAATGCCATACTGCAGTCCCAGTCGAATGCATAAGCGGACTGCAGTCCCAGTCGAATGCATAAGCGGACTGCAGTCCGA"
#one = "CGA"
#two = "CACGA"
##one = "ACT"
##two = "ACAGTCGAATGCATACAGTCCGTCCGA"
one = "MFP"
two = "FPMVSSSSS"   # will fail if student does 0,1,2 loop instead of 0,i+1,j+1 loop
##one = "FPW"
##two = "MPVVWPTLLDLSRDECKRILRKLELEAYAGVISALRAQGDLTKEKKDLLGELSKVLSISTERHRAEVRRA\
##VNDERLTTIAHNMSGPNSSSEWSIEGRRLVPLMPRLVPQTAFTVTANAVANAAIQHNASLPVPAETGSKE\
##VVCYSYTSTTSTPTSTPVPSGSIATVKSPRPASPASNVVVLPSGSTVYVKSVSCSDEDEKPRKRRRTNSS\
##SSSPVVLKEVPKAVVPVSKTITVPVSGSPKMSNIMQSIANSLPPHMSPVKITFTKPSTQTTNTTTQKVII\
##VTTSPSSTFVPNILSKSHNYAAVTKLVPTSVIASTTQKPPVVITASQSSLVSNSSSGSSSSTPSPIPNTV\
##AVTAVVSSTPSVVMSTVAQGVSTSAIKMASTRLPSPKSLVSAPTQILAQFPKQHQQSPKQQLYQVQQQTQ\
##QQVAQPSPVSHQQQPQQSPLPPGIKPTIQIKQESGVKIITQQVQPSKILPKPVTATLPTSSNSPIMVVSS\
##NGAIMTTKLVTTPTGTQATYTRPTVSPSIGRMAATPGAATYVKTTSGSIITVVPKSLATLGGKIISSNIV\
##SGTTTKITTIPMTSKPNVIVVQKTTGKGTTIQGLPGKNVVTTLLNAGGEKTIQTVPTGAKPAILTATRPI\
##TKMIVTQPKGIGSTVQPAAKIIPTKIVYGQQGKTQVLIKPKPVTFQATVVSEQTRQLVTETLQQASRVAE\
##AGNSSIQEGKEEPQNYTDSSSSSTESSQSSQDSQPVVHVIASRRQDWSEHEIAMETSPTIIYQDVSSESQ\
##SATSTIKALLELQQTTVKEKLESKPRQPTIDLSQMAVPIQMTQEKRHSPESPSIAVVESELVAEYITTER\
##TDEGTEVAFPLLVSHRSQPQQPSQPQRTLLQHVAQSQTATQTSVVVKSIPASSPGAITHIMQQALSSHTA\
##FTKHSEELGTEEGEVEEMDTLDPQTGLFYRSALTQSQSAKQQKLSQPPLEQTQLQVKTLQCFQTKQKQTI\
##HLQADQLQHKLPQMPQLSIRHQKLTPLQQEQAQPKPDVQHTQHPMVAKDRQLPTLMAQPPQTVVQVLAVK\
##TTQQLPKLQQAPNQPKIYVQPQTPQSQMSLPASSEKQTASQVEQPIITQGSSVTKITFEGRQPPTVTKIT\
##GGSSVPKLTSPVTSISPIQASEKTAVSDILKMSLMEAQIDTNVEHMIVDPPKKALATSMLTGEAGSLPST\
##HMVVAGMANSTPQQQKCRESCSSPSTVGSSLTTRKIDPPAVPATGQFMRIQNVGQKKAEESPAEIIIQAI\
##PQYAIPCHSSSNVVVEPSGLLELNNFTSQQLDDEETAMEQDIDSSTEDGTEPSPSQSSAERS"

find_alignment(one,two)




