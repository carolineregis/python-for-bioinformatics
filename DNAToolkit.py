import re

# DNA toolkit file

nucleotides = ["A", "C", "G", "T"]
doubleStrandDNAComplement = {"A": "T", "T": "A", "G": "C", "C": "G"}
RNAnucleotides = {"A": "U", "T": "U", "G": "C", "C": "G"}

# Check the sequence to ensure it's a valid DNA string
# A valid DNA string contains only ACTG elements
def validateSeq(dna_seq):
  tmpseq = dna_seq.upper() # DNA nucleotides are written in uppercase
  for nuc in tmpseq:
    if nuc not in nucleotides:
      return False
  return tmpseq;

# Counting nucleotides frequency (how many times it appears in the array)    
def countNucFrequency(seq):
  tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0} # initial object
  for nuc in seq: #loops through each nucleotide in the array
    tmpFreqDict[nuc] += 1 # adds an index in the object element relative to the nucleotide that's just been counted
  return tmpFreqDict

# Generating complementary DNA strand
def complementaryStrand(seq):
  return ''.join([doubleStrandDNAComplement[nuc] for nuc in seq])

# DNA Transcription
def transcription(seq):
 return ''.join([RNAnucleotides[nuc] for nuc in seq])