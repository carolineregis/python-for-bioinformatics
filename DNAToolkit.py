# DNA toolkit file

nucleotides = ["A", "C", "G", "T"]

# Check the sequence to ensure it's a valid DNA string
# A valid DNA string contains only ACTG elements

def validateSeq(dna_seq):
  tmpseq = dna_seq.upper() # DNA nucleotides are written in uppercase
  for nuc in tmpseq:
    if nuc not in nucleotides:
      return False
  return tmpseq;
    
