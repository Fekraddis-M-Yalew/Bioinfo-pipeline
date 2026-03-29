Bioinformatics pipeline assignment started


# Simple steps for variant module

import gzip

file = "variants.vcf.gz" 
total_variants = 0
with gzip.open(file, "rt") as f:
    for line in f:
        if not line.startswith("#"):  # skip header
            total_variants += 1
if total_variants > 0:
    print("Total variants found:", total_variants)
    print("Average variants per sample:", total_variants / 10)  # dummy
else:
    print("No variants found!")

