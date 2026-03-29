Bioinformatics pipeline assignment started

#simple steps for QC modules

import gzip

file = "sample.fastq.gz" # works for gz files
total_reads = 0
total_length = 0
with gzip.open(file, "rt") as f:
    for i, line in enumerate(f):
        if i % 4 == 1: # sequence line
            seq = line.strip()
            total_reads += 1
            total_length += len(seq)
if total_reads > 0:
    print("Total reads:", total_reads)
    print("Average length:", total_length / total_reads)
else:
    print("No reads found!")

