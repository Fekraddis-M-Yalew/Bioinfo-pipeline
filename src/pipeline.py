Bioinformatics pipeline assignment started


#simple steps for QC modules

import os
import gzip

file = "sample.fastq.gz"

if not os.path.exists(file):
    print(f"Error: {file} not found!")
    exit(1) 
 
total_reads = 0
total_length = 0
valid_nucleotide = set("ATCG")

with gzip.open(file, "rt") as f:
    for i, line in enumerate(f):
        if i % 4 == 1: 
            seq = line.strip()
            if not set(seq).issubset(valid_nucleotides):
                print(f"Warning: invalid characters found in sequence: {seq}")

            total_reads += 1
            total_length += len(seq)

if total_reads > 0:
    print("Total reads:", total_reads)
    print("Average length:", total_length / total_reads)
else:
    print("No reads found!")


# Simple steps for variant module

print("\n=== variant module ===")
import gzip

file = "variants.vcf.gz" 
total_variants = 0
with gzip.open(file, "rt") as f:
    for line in f:
        if not line.startswith("#"):  
            total_variants += 1
if total_variants > 0:
    print("Total variants found:", total_variants)
    print("Average variants per sample:", total_variants / 10)  
else:
    print("No variants found!")


