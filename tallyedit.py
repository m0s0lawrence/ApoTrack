import sys

def parse_mpileup_line(line):
    split_line = line.split("\t")
    ref_base = split_line[2].upper()

    bam_count = (len(split_line) - 3) // 3
    total_basecalls = [0] * bam_count
    total_edits = [0] * bam_count

    for i in range(bam_count):
        basecalls = split_line[4 + i * 3].upper()
        if ref_base in {'C', 'G'}:
            for basecall in basecalls:
                if basecall in {'.', ',', 'A', 'T', 'G', 'C'}:
                    total_basecalls[i] += 1
                    if (ref_base == 'C' and basecall == 'T') or (ref_base == 'G' and basecall == 'A'):
                        total_edits[i] += 1

    return ref_base, total_edits, total_basecalls

if __name__ == "__main__":
    bam_count = None
    total_edits = None
    total_basecalls = None
    ref_bases = set()

    for line in sys.stdin:
        if line.strip() != "":
            ref_base, edits, basecalls = parse_mpileup_line(line)
            ref_bases.add(ref_base)
            if bam_count is None:
                bam_count = len(edits)
                total_edits = [0] * bam_count
                total_basecalls = [0] * bam_count
            for i in range(bam_count):
                total_edits[i] += edits[i]
                total_basecalls[i] += basecalls[i]

    if ref_bases == {'N'}:
        print("Error: All reference bases are 'N'. Did you forget to include the reference FASTA in the samtools mpileup command?", file=sys.stderr)
        sys.exit(1)
        
    for i in range(bam_count):
        edit_rate = total_edits[i] / total_basecalls[i] if total_basecalls[i] > 0 else -1
        print(f"bam {i+1} editing rate per 1000 = {edit_rate * 1000:.2f}")


        
