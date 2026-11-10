import sys

MATCH = 1
MISMATCH = -1
GAP = -2

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

def findPaths(i, j, seq1, seq2, matrix):
    if matrix[i][j] == 0:
        return [("", "")]

    results = []

    if seq1[i - 1] == seq2[j - 1]:
        diagonal = matrix[i - 1][j - 1] + MATCH
    else:
        diagonal = matrix[i - 1][j - 1] + MISMATCH

    if matrix[i][j] == diagonal:
        for result1, result2 in findPaths(i - 1, j - 1, seq1, seq2, matrix):
            results.append((result1 + seq1[i - 1], result2 + seq2[j - 1]))

    if matrix[i][j] == matrix[i - 1][j] + GAP:
        for result1, result2 in findPaths(i - 1, j, seq1, seq2, matrix):
            results.append((result1 + seq1[i - 1], result2 + "-"))

    if matrix[i][j] == matrix[i][j - 1] + GAP:
        for result1, result2 in findPaths(i, j - 1, seq1, seq2, matrix):
            results.append((result1 + "-", result2 + seq2[j - 1]))

    return results

def smithWaterman(seq1, seq2):
    rows = len(seq1) + 1
    cols = len(seq2) + 1

    matrix = []
    for i in range(rows):
        matrix.append([0] * cols)

    maxScore = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if seq1[i - 1] == seq2[j - 1]:
                diagonal = matrix[i - 1][j - 1] + MATCH
            else:
                diagonal = matrix[i - 1][j - 1] + MISMATCH

            up = matrix[i - 1][j] + GAP
            left = matrix[i][j - 1] + GAP

            matrix[i][j] = max(0, diagonal, up, left)

            if matrix[i][j] > maxScore:
                maxScore = matrix[i][j]
                
    if maxScore == 0:
        return [], 0

    alignments = []

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == maxScore:
                alignments += findPaths(i, j, seq1, seq2, matrix)

    return alignments, maxScore

def saveResults(alignments, score):
    with open("output.txt", 'w') as file:
        if len(alignments) == 0:
            file.write("Brak dopasowań\n")
            return

        for result1, result2 in alignments:
            file.write(result1 + "\n")

            sign = ""
            for i in range(len(result1)):
                if result1[i] == result2[i]:
                    sign += "|"
                else:
                    sign += " "
            file.write(sign + "\n")

            file.write(result2 + "\n\n")
            

fastaFile = readArgs()
seq1, seq2 = readSeq(fastaFile)

alignments, score = smithWaterman(seq1, seq2)
saveResults(alignments, score)

print(f"Liczba dopasowań: {len(alignments)}")
print(f"Score = {score}")

