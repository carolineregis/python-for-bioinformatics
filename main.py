from DNAToolkit import *
import random

# Setting a DNA String
dnaStr = "ATTTC"

# Creating a random DNA String
# random runs 20 times through the nucleotides array and gets one item each time
randDNAStr = ''.join([random.choice(nucleotides)
                      for nuc in range(80)])

# Sequence length
print(f" [1] + Sequence length: {len(randDNAStr)}\n")

# Validating sequence
print(f" [2] + Validating sequence: {validateSeq(randDNAStr)}\n")

# Counting nucleotides
print(f" [3] + Counting nucleotides: {countNucFrequency(randDNAStr)}\n")

# Generating complementary strand for DNA
print (f" [4] + Generating complementary strand to DNA:\n5' {randDNAStr} 3'")
print (f"   {''.join(['|' for c in range(len(randDNAStr))])}")
print (f"3' {complementaryStrand(randDNAStr)} 5'\n")

# Transcription 
print(f" [5] + DNA transcription {transcription(randDNAStr)}")