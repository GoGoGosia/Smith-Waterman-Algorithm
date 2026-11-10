import sys

def readArgs():
    if len(sys.argv) < 2:
        print("Podaj plik .fasta")
        sys.exit(1)
        
    if sys.argv[1] == "--fasta":
        if len(sys.argv) < 3:
           print("Podaj plik .fasta") 
        sys.exit(1)
        return sys.argv[2]
    
    return sys.argv[1]

def readSeq(filename):
    sequences = []
    currentSeq = ""
    
    with open(filename) as file:
        for line in file:
            line = line.strip() 
            
            if line == "":
                continue 
            
            if line.startswith(">"):
                if currentSeq != "":
                    sequences.append(currentSeq)
                    currentSeq = "" 
            else:
                currentSeq = currentSeq + line
                
    if currentSeq != "":
        sequences.append(currentSeq)

    if len(sequences) != 2:
        print("Plik musi zawierać 2 sekwencje")
        sys.exit(1)
        
    return sequences[0], sequences[1]


fastaFile = readArgs()
seq1, seq2 = readSeq(fastaFile)
