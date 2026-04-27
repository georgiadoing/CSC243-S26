# Make a dictionary to look up list of codons for given a.a.
def makeCodonList():
    Ccodons = ["TGC","TGT"]
    Scodons = ["AGC","AGT","TCA","TCC","TCG","TCT"]
    Tcodons = ["ACA","ACC","ACG","ACT"]
    Pcodons = ["CCA","CCC","CCG","CCT"]
    Acodons = ["GCA","GCC","GCG","GCT"]
    Gcodons = ["GGA","GGC","GGG","GGT"]
    Ncodons = ["AAC","AAT"]
    Dcodons = ["GAC","GAT"]
    Ecodons = ["GAA","GAG"]
    Qcodons = ["CAA","CAG"]
    Hcodons = ["CAC","CAT"]
    Rcodons = ["AGA","AGG","CGA","CGC","CGG","CGT"]
    Kcodons = ["AAA","AAG"]
    Mcodons = ["ATG"]
    Icodons = ["ATA","ATC","ATT"]
    Lcodons = ["TTA","TTG","CTA","CTC","CTG","CTT"]
    Vcodons = ["GTA","GTC","GTG","GTT"]
    Fcodons = ["TTC","TTT"]
    Ycodons = ["TAC","TAT"]
    Wcodons = ["TGG"]
    return {"C":Ccodons, "S":Scodons, "T":Tcodons, "P":Pcodons, "A":Acodons, "G":Gcodons,
     "N":Ncodons, "D":Dcodons, "E":Ecodons, "Q":Qcodons, "H":Hcodons, "R":Rcodons,
     "K":Kcodons, "M":Mcodons, "I":Icodons, "L":Lcodons, "V":Vcodons, "F":Fcodons,
     "Y":Ycodons, "W":Wcodons}


CodonList = makeCodonList()

#example: codon list for Valine:
print(CodonList["V"])

